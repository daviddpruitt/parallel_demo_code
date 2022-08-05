#!/usr/bin/env python3
import pymp
 
def count_words(wordlist):
    dumblist = ['love', 'time', 'spent']    
    wc = pymp.shared.dict()

    #init the dictionary for results
    for word in wordlist:
        wc[word]= 0
            
    with pymp.Parallel(3) as p:

        for w in p.iterate(dumblist):
            print(f'thread {p.thread_num} getting {w}')

    return wc


def main():
    wordlist = ["love", "the", "time", "we", "spent", "every", "poetry"]
    
    wordcount = count_words(wordlist)
    print(wordcount)

    
if __name__ == '__main__':
    # execute only if run as a script
    main()

