import re, time
import pymp as pmp

class MapReduce(object):

    def __init__(self,cpuModel):
        self.cpuModel = cpuModel
        pass

    def _count_occurrences(self, filename: str):
        result = dict()
        words = []
        with open(filename, "r") as f:
            for w in f.readlines():
                w = w.lower()
                w = re.sub(r'([^a-zA-Z\s]+?)', '', w)  # REMOVE SPECIAL CHARACTERS TODO: alphanumeric?
                # w = w.strip().replace("\\s+", "").replace(".", "").replace(",", "").replace("\n", "").replace(":", "")
                words.append(w.split())
        # Flatten List
        words = sum(words, [])
        testText = " ".join(words)
        for w in words:
            result[w] = len(re.findall(w, testText))

        return result

    def fileAgglomeration(self, dataset: list):
        """
        All files that will be processed and return a result map.
        """
        result = dict()

        startTimeForAgglomeration = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
        print("CPU Model,Index, Filename, Elapsed Time")
        for idx, e in enumerate(dataset):
            # CPU TIME
            startTime = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
            result[idx] = self._count_occurrences(filename=e)
            endTime = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)

            # CPU Model, Index, Filename, Time Taken Processing File
            fileName = e.split("/")[-1]
            print(f"{self.cpuModel},{idx + 1},{fileName},{endTime - startTime}")  # Logger ^ Markdown

        endTimeForAgglomeration = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
        print(
            f"Total Files Aggregated: {len(dataset)} and total {endTimeForAgglomeration - startTimeForAgglomeration} seconds elapsed.")

        return result


    def mapReduce(self, allResults: dict):
        print("Map Reduce")
        result = dict()
        startTime = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
        for e in allResults.values():
            for k, v in e.items():
                if k not in result.keys():
                    result[k] = v
                else:
                    result[k] += v
        endTime = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
        print(f"Map Reduce Seconds Elapsed: {endTime - startTime} of {len(allResults)} files.")
        return result
