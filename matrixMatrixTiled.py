#!/usr/bin/env python3
import argparse
import time
import pymp
from matrixUtils import *

tileSize = 16

def matMatMultiply(a, b, c):
    size = len(a)

    for i in range(size):
        for j in range(size):
            for k in range(size):
                c[i][j] =  c[i][j] + a[i][k] * b[k][j]
    return c

def copyToLocal(globalMatrix, localMatrix, i_tile, j_tile, size):
    i_start = i_tile * tileSize
    j_start = j_tile * tileSize
    for i in range(size):
        i_global = i_start + i
        for j in range(size):
            j_global = j_start + j
            localMatrix[i][j] = globalMatrix[i_global][j_global]

def copyToGlobal(localMatrix, globalMatrix, i_tile, j_tile, size):
    i_start = i_tile * tileSize
    j_start = j_tile * tileSize
    for i in range(size):
        i_global = i_start + i
        for j in range(size):
            j_global = j_start + j
            globalMatrix[i_global][j_global] = localMatrix[i][j]

def matMatMultiplyTile(a, b, c):
    size = len(a)
    numTiles = size // 16

    for kk in range(0, size, tileSize):
        for jj in range(0, size, tileSize):
            for i in range(0, size):
                j_end = jj + tileSize
                for j in range(jj, j_end):
                    k_end = kk + tileSize
                    sum = c[i][j]
                    for k in range(kk, k_end):
                        sum += a[i][k] * b[k][j]
                    c[i][j] = sum

def matMatMultiplyTilePara(a, b, c):
    size = len(a)
    numTiles = size // 16

    with pymp.Parallel() as p:
        if p.thread_num is 0:
            print(f"Doing tiled matrix multiply using {p.num_threads} threads")
        for kk in p.range(0, size, tileSize):
            for jj in range(0, size, tileSize):
                for i in range(0, size):
                    j_end = jj + tileSize
                    for j in range(jj, j_end):
                        k_end = kk + tileSize
                        sum = c[i][j]
                        for k in range(kk, k_end):
                            sum += a[i][k] * b[k][j]
                        c[i][j] = sum


def setupMatrix(size):
    c = genMatrix(size, 0)
    return c

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
    parser.add_argument('-i', '--ident', action='store_true',
        help='The value with which to fill the second array with')
    parser.add_argument('-p', '--para', action='store_true',
        help='If the code should run the openmp parallel version')
    parser.add_argument('-n', '--num_iters', default=10, type=int,
        help='The value with which to fill the second array with')
    parser.add_argument('-t', '--tiled', action='store_true',
        help='If the code should run the tiled version')

    args = parser.parse_args()
    size = args.size
    a_vals = args.avalue
    b_vals = args.bvalue
    ident = args.ident
    para = args.para
    iters = args.num_iters

    print('Generating matrices')
    print(f'Size {size}')
    print(f'A values {a_vals}')
    a = genMatrix(size, a_vals)
    if ident:
        print(f'B as identity')
        b = genIdentMatrix(size)
    else:
        print(f'B values {b_vals}')
        b = genMatrix(size, b_vals)

    if para is True:
        avgTime = 0
        for trial in range(iters):
            c = result = pymp.shared.array((size, size), dtype='uint16') #setupMatrix(len(a))
            startTime = time.clock_gettime(time.CLOCK_MONOTONIC)
            matMatMultiplyTilePara(a, b, c)
            elapsedTime = time.clock_gettime(time.CLOCK_MONOTONIC) - startTime
            avgTime += elapsedTime

        avgTime /= iters

        print(f'Parallel block time {avgTime} seconds')
        printSubarray(c, 10)
    else:
        avgTime = 0
        for trial in range(iters):
            print(f'Trial {trial}')
            c = setupMatrix(len(a))
            startTime = time.clock_gettime(time.CLOCK_MONOTONIC)
            matMatMultiplyTile(a, b, c)
            elapsedTime = time.clock_gettime(time.CLOCK_MONOTONIC) - startTime
            avgTime += elapsedTime

        avgTime /= iters

        print(f'Blocked time {avgTime} seconds')
        printSubarray(c, 10)


if __name__ == '__main__':
    # execute only if run as a script
    main()
