from matrixUtils import genMatrix, genRandomMatrix, writeToFile, multiplyMatrix

#Debugger
import numpy as np


if __name__ == "__main__":

    A = genMatrix(4,100)
    B = genMatrix(4,2)

    result = multiplyMatrix(A,B)
    result2 = np.matmul(A,B)

    print(result)
    print(result2)
    writeToFile(result,"result.txt")
