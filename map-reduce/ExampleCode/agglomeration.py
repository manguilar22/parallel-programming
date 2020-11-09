import re, time
import pymp as pmp


# Sequential Version ( COUNT ALL WORDS )
def count_occurrences(filename:str):
    result = dict()
    words = []
    with open(filename,"r") as f:
        for w in f.readlines():
            w = w.lower()
            w = re.sub(r'([^a-zA-Z\s]+?)', '', w) # REMOVE SPECIAL CHARACTERS TODO: alphanumeric?
            words.append(w.split())
    # Flatten List
    words = sum(words,[])
    testText = " ".join(words)
    for w in words:
        result[w] = len(re.findall(w,testText))

    return result

# Go through each list and count all words occurring
def fileAgglomeration(cpuModel:str,dataset:list):
    """
    Sequential Version
    :return dict(0=dict(...),1=dict(...),2=dict(...),...) | len(dataset)
    """
    result = dict()
    startTimeForAgglomeration = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    print("CPU Model,Index, Filename, Elapsed Time")
    for idx, e in enumerate(dataset):
        # CPU TIME
        startTime = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
        result[idx] = count_occurrences(filename=e)
        endTime = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
        # CPU Model, Index, Filename, Time Taken Processing File        # Logger ^ Markdown
        fileName = e.split("/")[-1]
        print(f"{cpuModel},{idx + 1},{fileName},{endTime - startTime}")  # Logger ^ Markdown

    endTimeForAgglomeration = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    print(f"Total Files Aggregated: {len(dataset)} and total {endTimeForAgglomeration-startTimeForAgglomeration} seconds elapsed.")

    return result


################################################################################################
async def fileAgglomerationAsync(cpuModel:str,dataset:list):
    """
        All files that will be processed and return a result map.
        """
    result = dict()

    startTimeForAgglomeration = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    print("CPU Model,Index, Filename, Elapsed Time")
    for idx, e in enumerate(dataset):
        # CPU TIME
        startTime = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
        result[idx] = await count_occurrencesAsync(filename=e)
        endTime = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)

        # CPU Model, Index, Filename, Time Taken Processing File
        fileName = e.split("/")[-1]
        print(f"{cpuModel},{idx + 1},{fileName},{endTime - startTime}")  # Logger ^ Markdown

    endTimeForAgglomeration = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    print(
        f"Total Files Aggregated: {len(dataset)} and total {endTimeForAgglomeration - startTimeForAgglomeration} seconds elapsed.")

    return result


async def count_occurrencesAsync(filename:str):
    result = dict()
    words = []
    with open(filename,"r") as f:
        for w in f.readlines():
            w = w.lower()
            w = re.sub (r'([^a-zA-Z\s]+?)', '', w) # REMOVE SPECIAL CHARACTERS TODO: alphanumeric?
            #w = w.strip().replace("\\s+", "").replace(".", "").replace(",", "").replace("\n", "").replace(":", "")
            words.append(w.split())
    # Flatten List
    words = sum(words,[])
    testText = " ".join(words)
    for w in words:
        result[w] = len(re.findall(w,testText))

    return result