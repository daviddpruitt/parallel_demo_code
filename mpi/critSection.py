#!/usr/bin/env python3

import time
import pymp

def sumOnes(count = 100):

    sum = pymp.shared.list([0])
    
    with pymp.Parallel(2) as p:
        # get a lock for this parallel region
        sumLock = p.lock
        for i in p.range(0, count):
            # removing these locks leads to an incorrect sum
            sumLock.acquire()

            sum[0] = sum[0] + 1

            # removing just the release will result in
            # deadlock
            sumLock.release()

    return sum

def main():
    """
    main function for when running as a script
    """
    
    count = 10000

    sum = sumOnes(count)
    print(f'summing {count} ones using sum {sum}')
    
if __name__ == '__main__':
    # execute only if run as a script
    main()

