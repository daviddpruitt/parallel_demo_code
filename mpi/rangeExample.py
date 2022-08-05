#!/usr/bin/env python3

import time
import pymp


def main():
    """
    main function for when running as a script
    """

    with pymp.Parallel() as p:
        listOfNums = []
        for number in p.range(0, 16):
            listOfNums.append(number)

        print(f'List of numbers that thread {p.thread_num} got {listOfNums}')
    #print(f'List of numbers {listOfNums}')

    
if __name__ == '__main__':
    # execute only if run as a script
    main()
