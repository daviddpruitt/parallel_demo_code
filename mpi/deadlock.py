from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank is 0:
    msg = "Hello from thread 0!"


    print('Thread 0 receving message')
    recvd_msg = comm.recv(source=1, tag=1)
    print(f'Thread 0 received message: {recvd_msg}')


    print('Thread 0 sending message')
    comm.isend(msg, dest=1, tag=1)

elif rank is 1:
    msg = "Hello from thread 1!"

    print('Thread 1 receving message')
    recvd_msg = comm.recv(source=0, tag=1)
    print(f'Thread 1 received message: {recvd_msg}')

    print('Thread 1 sending message')
    comm.send(msg, dest=0, tag=1)
