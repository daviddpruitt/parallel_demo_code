# import the PyMP library
import pymp
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank() # get thread number
size = comm.Get_size() # get number of threads


msg = ""
if size > 1 and rank == 0:
    print('Thread 0 saying hello')
    comm.send(msg, dest=1, tag=42)
elif size > 1 and rank is 1:
    msg = comm.recv(source=0, tag=42)

# start a openmp parallel section
with pymp.Parallel() as p:
    # print the thread number and number of threads
    # p.thread_num is the current thread number
    # p.num_threads is the total number of threads in the set
    print(f'MPI thread {rank} omp thread {p.thread_num} of {p.num_threads}')
    if p.thread_num == 0:
        print(f' Received message {msg}')
    
