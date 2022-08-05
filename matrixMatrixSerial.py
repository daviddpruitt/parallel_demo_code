#!/usr/bin/env python3

import matrixUtils
import numpy as np
import time

def matMatMul(matA, matB):
    """
    Multiplies matrices A and B and returns the result
    This function assumes a and b are square
    """

    length = len(matA)

    result = [[0 for col in range(0, length)] for row in range(0,length)]

    for col in range(0, length):
        for row in range(0, length):
            sum = 0
            for k in range(0, length):
                sum = sum + matA[col][k] * matB[k][row]
            result[col][row] = sum

    return result

def main():
    """
    main function for when running as a script
    """

    print('Getting input matrices...')

    startTime = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    #matA = matrixUtils.genMatrix(512,1)
    matA = matrixUtils.readFromFile('matA512.txt')

    #matB = matrixUtils.genMatrix(512,1)
    matB = matrixUtils.readFromFile('matB512.txt')
    endTime = time.clock_gettime( time.CLOCK_THREAD_CPUTIME_ID )

    elapsedReadTime = endTime - startTime
    print('Multiplying matrices...')

    startTime = time.clock_gettime( time.CLOCK_THREAD_CPUTIME_ID )
    matC = matMatMul(matA, matB)
    endTime = time.clock_gettime( time.CLOCK_THREAD_CPUTIME_ID )

    print(f'Time to get matrices {elapsedReadTime:.2f} seconds')
    print(f'Elapsed time {endTime - startTime:.2f} seconds')

    print('Result')
    matrixUtils.printSubarray(matC)


if __name__ == '__main__':
    # execute only if run as a script
    main()
