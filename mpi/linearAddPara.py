#!/usr/bin/env python3

import numpy as np
import time
import pymp

def linearFMA(vectorA, vectorB, constant):
    """
    Adds two vectores together
    """

    length = len(vectorA)

    #result = [0 for i in range(0, length)]

    result = pymp.shared.array((length, ), dtype='uint16')

    with pymp.Parallel() as p:
        if p.thread_num is 0:
            print(f'Executing using {p.num_threads} threads')

        output = []
        for x in p.range(0, length):
            #result[x] = vectorA[x] + vectorB[x]
            output.append(x)

        print(f'Thread {p.thread_num}\n{output}')

    return result

def main():
    """
    main function for when running as a script
    """

    length = 32

    print('Generating vectors')

    vectorA = [1 for i in range(0, length)]
    vectorB = [1 for i in range(0, length)]

    print('Adding vectors')

    result = linearFMA(vectorA, vectorB, 2)

    # print first 4
    for i in range(0, 4):
        print(f'{result[i]}', end='')

    print('')

    # print first 4
    for i in range(length - 4, length):
        print(f'{result[i]}', end='')

    print('')

if __name__ == '__main__':
    # execute only if run as a script
    main()
