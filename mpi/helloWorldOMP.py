#!/usr/bin/env python3

import pymp

def main():
    with pymp.Parallel() as p:
        print(f'Hello from thread {p.thread_num} of {p.num_threads}')

if __name__ == '__main__':
        # execute only if run as a script
        main()
