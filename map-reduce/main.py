import os, re

# Time CPU
import time

dataset = [os.path.join(os.getcwd(),f"dataset/{e}") for e in os.listdir("./dataset/")]

cpuModel = os.getenv("CPUMODEL") if os.getenv("CPUMODEL") else "Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz"

from ExampleCode.count import count_occurrencesWithSpecefiedWords,count_occurrencesWithSpecefiedWordsParallel

if __name__ == "__main__":
    # Parallel Test
    for thread in [2,4,8]:
        print(f"Parallel with {thread} threads.")
        parallelResults = count_occurrencesWithSpecefiedWordsParallel(cpuModel=cpuModel,fileDirectory=dataset,num_threads=thread)
    print("Sequential Version")
    result = count_occurrencesWithSpecefiedWords(cpuModel=cpuModel,fileDirectory=dataset)
    print("--- (Sequential) Check Answers")
    for k,v in result.items():
        print(f"{k} : {v}")
    print("--- (Parallel) Check Answers")
    for k,v in parallelResults.items():
        print(f"{k} : {v}")
