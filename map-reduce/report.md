# Map Reduce 


## CPU Model 

```
model name      : Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz
      4      36     216
```

### Total Results 

Parallel with 2 threads.
(Parallel) Map Reduce time elapsed: 1348.7914639469998

Parallel with 4 threads.
(Parallel) Map Reduce time elapsed: 1246.5341840620001

Parallel with 8 threads.
(Parallel) Map Reduce time elapsed: 1277.241349168

Total 31025 individual words inside the 8 files.

### Word count of selected words 

* hate : 332
* love : 3070
* death : 1016
* night : 1402
* sleep : 470
* time : 1806
* henry : 661
* hamlet : 475
* you : 23306
* my : 14203              (**my,14205**)
* blood : 1009
* poison : 139
* macbeth : 288
* king : 4545
* heart : 1458            (**heart,1463**)
* honest : 434


### Sequential Version 


#### i5-6200U CPU
Total Files Aggregated: 8 and total 1279.393797639 seconds elapsed.

#### i7-3720QM CPU 
Total Files Aggregated: 8 and total 933.957277147 seconds elapsed.


| CPU MODEL | File Index | File Name | Seconds Elapsed|
|-----------|------------|-----------|----------------|
|Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz|1|shakespeare1.txt|2.849022381|
|Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz|2|shakespeare2.txt|307.392208052|
|Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz|3|shakespeare3.txt|23.014888482000003|
|Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz|4|shakespeare4.txt|147.990857421|
|Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz|5|shakespeare7.txt|170.68927713699998|
|Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz|6|shakespeare5.txt|231.69239651700002|
|Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz|7|shakespeare8.txt|141.26035856200008|
|Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz|8|shakespeare6.txt|254.50464607999993|
|Intel(R) Core(TM) i7-3720QM CPU @ 2.60GHz|1|shakespeare7.txt|125.223561155|
|Intel(R) Core(TM) i7-3720QM CPU @ 2.60GHz|2|shakespeare8.txt|100.773393171|
|Intel(R) Core(TM) i7-3720QM CPU @ 2.60GHz|3|shakespeare6.txt|181.797388708|
|Intel(R) Core(TM) i7-3720QM CPU @ 2.60GHz|4|shakespeare4.txt|108.2532517309999|
|Intel(R) Core(TM) i7-3720QM CPU @ 2.60GHz|5|shakespeare3.txt|18.24238250999997|
|Intel(R) Core(TM) i7-3720QM CPU @ 2.60GHz|6|shakespeare1.txt|2.353841564999925|
|Intel(R) Core(TM) i7-3720QM CPU @ 2.60GHz|7|shakespeare2.txt|228.32216070200002|
|Intel(R) Core(TM) i7-3720QM CPU @ 2.60GHz|8|shakespeare5.txt|168.99102055599997|

#### Map Reduce i7-3720QM CPU 
Map Reduce Seconds Elapsed: 0.025090522000027704 of 8 files.
