#!/usr/bin/env python3

import matrixUtils
import numpy as np
import time
import pymp
import argparse

def matMatMul(matA, matB):
    """
    Multiplies matrices A and B and returns the result
    This function assumes a and b are square
    """

    length = len(matA)

    output = [[0 for col in range(0, length)] for row in range(0,length)]
    #result = [[0 for col in range(0, length)] for row in range(0,length)]
    result = pymp.shared.array((length, length), dtype='uint16')
    #result = pymp.shared.list()
    #for col in range(0, length):
    #    result.append([0 for row in range(0, length)])

    #print(result[0][0])
    #print(len(result))
    #print(len(result[0]))
    #print(result[127][127])
    #return result
    with pymp.Parallel() as p:
        if p.thread_num is 0:
            print(f"Executing using {p.num_threads} threads")
        for col in p.range(0, length):
            for row in range(0, length):
                sum = 0
                for k in range(0, length):
                    #if p.thread_num == 0:
                        #print(f'k {k}')
                    sum = sum + matA[col][k] * matB[k][row]
                    #print('saving to result')
                    result[col][row] = sum

    return result

def main():
    """
    Used for running as a script
    """

    parser = argparse.ArgumentParser(description=
        'Generate a 2d matrix and save it to  a file.')
    parser.add_argument('-s', '--size', default=1024, type=int,
        help='Size of matrices to multiply')
    parser.add_argument('-a', '--avalue', default=1, type=int,
        help='The value with which to fill the first array with')
    parser.add_argument('-b', '--bvalue', default=1, type=int,
        help='The value with which to fill the second array with')
    parser.add_argument('-n', '--num_iters', default=10, type=int,
        help='The value with which to fill the second array with')

    parser.add_argument('-i', '--ident', action='store_true',
        help='The value with which to fill the second array with')


    args = parser.parse_args()
    size = args.size
    a_vals = args.avalue
    b_vals = args.bvalue
    ident = args.ident
    iters = args.num_iters

    length = size

    print(f'Multiplying {size}x{size} matrices {iters} times')
    print('Getting input matrices...')

    elapsedReadTime = 0
    elapsedTime = 0
    for i in range(iters):
        startTime = time.clock_gettime(time.CLOCK_MONOTONIC)
        matA = matrixUtils.genMatrix(length,1)
        #matA = matrixUtils.readFromFile('matA.txt')

        matB = matrixUtils.genMatrix(length,1)
        #matB = matrixUtils.readFromFile('matB.txt')
        endTime = time.clock_gettime(time.CLOCK_MONOTONIC)

        elapsedReadTime = elapsedReadTime + endTime - startTime
        print('Multiplying matrices...')

        startTime = time.clock_gettime(time.CLOCK_MONOTONIC)
        matC = matMatMul(matA, matB)
        endTime = time.clock_gettime(time.CLOCK_MONOTONIC)
        elapsedTime = elapsedTime + endTime - startTime

    elapsedReadTime = elapsedReadTime / iters
    elapsedTime = elapsedTime / iters

    print(f'Time to get matrices {elapsedReadTime:.2f} seconds')
    print(f'Elapsed time {elapsedTime:.2f} seconds')

    print('Result UL')
    matrixUtils.printSubarray(matC)

    print()
    print('Result LR')
    matrixUtils.printSubarray(matC, startPos = length - 10)

if __name__ == '__main__':
    # execute only if run as a script
    main()
