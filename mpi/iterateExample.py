#!/usr/bin/env python3

import time
import pymp

def dictOfItems(itemsToIterate=[]):
    zeros = [i for i in range(0, len(itemsToIterate))]
    listOfZeros = zip(itemsToIterate, zeros)
    # print(zeros)
    # print(itemsToIterate)
    # for zero in listOfZeros:
    #     print(zero)
    
    sharedDict = pymp.shared.dict( listOfZeros )
    
    with pymp.Parallel() as p:
        listOfItems = []
        #print(sharedDict)
 
        # iterate over the list of items
        for item in p.iterate(itemsToIterate):
            
            # for each item take that item and
            # add thread_num of these to the dict
            listOfItems.append(item * (p.thread_num + 1))

        # add the list to the dict
        sharedDict[p.thread_num] = listOfItems

    return sharedDict
        
def main():
    """
    main function for when running as a script
    """

    itemsToIterate = ['A', 'B', 'C', 'D',
                      'E', 'F', 'G', 'H']
    lists = dictOfItems(itemsToIterate)

    for list in lists:
        print(f'{list} : {lists[list]}')
    
if __name__ == '__main__':
    # execute only if run as a script
    main()

