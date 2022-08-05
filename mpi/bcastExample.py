from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

msg = "Nothing here"

bcast_sender = 0  # AKA root

if rank is 0:
    msg = "Hi Everybody!"

recv_msg = comm.bcast(msg, root=bcast_sender)

print(f'Thread {rank} from {bcast_sender} received: {recv_msg}')

    
