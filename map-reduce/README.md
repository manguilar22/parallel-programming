# Parallel-Computing-MapReduce
For this assignment you will write a parallel map reduce program. The program will search for a set 
of words among a set of documents that constitute the works of Shakespeare. The set of words is listed 
below. The assignment should use the map-reduce design pattern to split up the work. You should have
functions that count the number of a specific word within a specific document and combine the individual
word counts.

The program should output the total instances of all words and the counts for each individual word

Word list:
hate, love, death, night, sleep, time, henry, hamlet, you, my, blood, poison, macbeth, king, heart, honest

Once completed the repository should contain your code, a short report, and any instructions needed to run your code.

Hints: 
* Its easier to load all the files containing text serial before entering the parallel processing region
* Some of the variables will need to be locked before updating, otherwise a difficult to debug race condition may occure
* This will take multiple loops (functions would be better though), you can iterate over the list of words

## Run the program. 

```bash 
python main.py > results.txt 
```
