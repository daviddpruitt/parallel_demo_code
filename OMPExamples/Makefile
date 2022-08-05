linearAdd: linearAddMain.o linearAdd.o
	clang++ $^ -fopenmp -o $@

linearAdd.o: linearAdd.cpp
	clang++ -c $^ -fopenmp -o $@

linearAddMain.o: linearAddMain.cpp
	clang++ -c $^ -o $@

clean:
	rm -f *.o linearAdd
