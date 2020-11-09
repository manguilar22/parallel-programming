# Flyod-Warshall Algorithm 

#### Results 

* Thread Number: 1
    * Time Elapsed: 0.53466928 seconds.
* Thread Number: 2
    * Time Elapsed: 0.40253266 seconds.
* Thread Number: 3
    * Time Elapsed: 0.531130726 seconds.
* Thread Number: 4
    * Time Elapsed: 0.373942955 seconds.
* Thread Number: 5
    * Time Elapsed: 0.40765158500000004 seconds.

#### Current CPU  

```
model name      : Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz
      4      36     216
```


### Install 

**~$** conda install mpi4py 

**~$** which mpirun
/usr/local/bin/anaconda3/envs/parallel/bin/mpirun 

**~$** mpirun -n 4 python main.py 
