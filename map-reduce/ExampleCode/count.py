import re, time
import pymp as pmp

checkTheseWords = ["hate", "love", "death", "night", "sleep", "time", "henry", "hamlet", "you", "my",  "poison", "macbeth", "king", "heart", "honest"]

# Parallel Version ( Count all word occurrences based on a list of existing words. )
def count_occurrencesWithSpecefiedWordsParallel(cpuModel:str,fileDirectory:list,words:list=checkTheseWords,num_threads:int=8):
    result = pmp.shared.dict()
    allWords = pmp.shared.list()
    # Agglomeration
    #print("|CPU Model|Filename|Elapsed Time|Thread|\n|---|---|---|---|")
    startReadingFilesTime = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    with pmp.Parallel(num_threads=num_threads) as p:
        for fileName in p.iterate(fileDirectory):
            with open(fileName,"r") as f:
                for w in f.readlines():
                    w = w.lower()
                    w = re.sub(r'([^a-zA-Z\s]+?)', '', w)
                    allWords.append(w.split())
            #p.print(f"|{cpuModel}|{fileName}|{endTime-startTime}|{p.thread_num}|")

    endReadingFilesTime = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    # Flatten List
    allWords = sum(allWords,[])
    allText = " ".join(allWords)
    # Reduction Step
    myTemp = 0
    startTimeReduce = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    with pmp.Parallel(num_threads=num_threads) as p:
        myLock = p.lock
        myTemp = 0
        for e in p.iterate(words):
            #myTemp = allText.find(e)
            myLock.acquire()
            myTemp = len(re.findall(e,allText))
            myLock.release()

            result[e] = myTemp


    endTimeReduce = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    print(f"(Parallel) Total Seconds elapsed reading files: {endReadingFilesTime-startReadingFilesTime} seconds.")
    print(f"(Parallel) Map Reduce time elapsed: {endTimeReduce-startTimeReduce} seconds.")
    return result


# Sequential Version
def count_occurrencesWithSpecefiedWords(cpuModel:str,fileDirectory:list, words:list=checkTheseWords,banner:bool=False):
    result = dict()
    allWords = []
    if banner:
        print("CPU Model,Index, Filename, Elapsed Time")
    # Agglomeration
    for idx, fileName in enumerate(fileDirectory):
        # Logging
        name = fileName.split("/")[-1]
        startTime = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
        with open(fileName,"r") as f:
            for w in f.readlines():
                w = w.lower()
                w = re.sub(r'([^a-zA-Z\s]+?)', '', w)
                allWords.append(w.split())
        endTime = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
        if banner:
            print(f"{cpuModel},{idx+1},{name},{endTime-startTime}")
    allWords = sum(allWords,[])
    allText = " ".join(allWords)
    # Reduce Step
    startTimeReduce = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    for e in words:
        result[e] = len(re.findall(e,allText))
    endTimeReduce = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    print(f"Map Reduce time elapsed: {endTimeReduce-startTimeReduce} seconds")
    return result
