from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank() # get thread number
size = comm.Get_size() # get number of threads

msg = "Hello thread 1!"

if rank is 0:
    print('Thread 0 sending message')
    comm.send(msg, dest=3, tag=42)
elif rank is 3:
    data = comm.recv(source=0, tag=42)
    print('Thread 1 received message')
    print(data)
else:
    print(f'Thread {rank} not sending or receiving')
