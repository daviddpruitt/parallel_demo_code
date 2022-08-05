from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = (rank+1)**2
data = comm.gather(data, root=0)

dict = {'rank':rank, 'data':data}

dicts = comm.gather(dict, root=0)
if rank == 0:
    print(f'Data: {data}')
    for i in range(size):
        assert data[i] == (i+1)**2
else:
    assert data is None

if rank == 0:
    print(f'Dict: {dicts}')

