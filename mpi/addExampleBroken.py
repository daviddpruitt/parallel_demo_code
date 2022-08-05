#!/usr/bin/env python3

import pymp


def main():
    """
    main function for when running as a script
    """

    listOfNumsA = [num for num in range(0,10)]
    listOfNumsB = [num for num in range(0,10)]

    sums = [0 for i in range(len(listOfNumsA))]
            
    with pymp.Parallel() as p:
        for index in p.range(len(listOfNumsA)):
            sums[index] = listOfNumsA[index] + listOfNumsB[index]

    print(f'Summed list {sums}')
            
    
if __name__ == '__main__':
    # execute only if run as a script
    main()
