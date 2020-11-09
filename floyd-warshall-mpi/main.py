from mpi4py import MPI
import math
import time

from utils import readFromFile, writeToFile

def floydWarshall(matrixFileName:str, resultFileName:str):
        # Get broadcast communicator
        comm = MPI.COMM_WORLD
        # Get Rank
        rank = comm.Get_rank()
        # Get Size
        size = comm.Get_size()
        # Get Full Matrix
        matrix = readFromFile(matrixFileName)

        # Formulas
        matrix_length = len(matrix)

        row = matrix_length // size

        threadsRow = size / matrix_length

        rowStart = math.trunc(row*rank)

        rowEnd = math.trunc(row*(rank + 1))

        # Calculation: Shortest Distance
        for k in range(len(matrix)):
            startRow = int(threadsRow * k)
            matrix[k] = comm.bcast(matrix[k], root=startRow)

            for x in range(rowStart, rowEnd):
                for y in range(len(matrix)):
                    matrix[x][y] = min(int(matrix[x][y]), (int(matrix[x][k]) + int(matrix[k][y])))

        # Agglomeration
        if comm.Get_rank() == 0:
            for k in range(rowEnd, len(matrix)):
                startRow = int(threadsRow * k)
                matrix[k] = comm.recv(source=startRow, tag=k)
            writeToFile(matrix,resultFileName)
        else:
            for k in range(rowStart, rowEnd):
                comm.send(matrix[k], dest=0, tag=k)

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    print(f"Thread Number: {comm.Get_rank()+1}")

    # Execute and Time Algorithm
    startTime = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    floydWarshall("./fwTest.txt", "./fwRESULT.txt")
    endTime = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)

    print(f"Time Elapsed: {(endTime-startTime)} seconds.")


