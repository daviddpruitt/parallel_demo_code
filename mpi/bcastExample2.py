from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

msg = "Nothing here"
ret_msg = ""

bcast_sender = 0  # AKA root

if rank is 0:
    msg = "Hi Everybody!"
else:
    ret_msg = "Hi Doctor Nick!"

ret_msg = comm.bcast(msg, root=bcast_sender)

print(f'msg {msg}')
print(f'Thread {rank} from {bcast_sender} received: {ret_msg}')

#recv_msg = comm.gather(ret_msg, root=bcast_sender)

#print(recv_msg)
#if rank is 0:
#    for msg in recv_msg:
#        print(msg)
