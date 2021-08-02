$(pro)
main: testbench.o  numericalDifferentation.o
	cc -o main testbench.o numericalDifferentation.o
testbench.o: testbench.c numericalDifferentation.h
	cc -c testbench.c
numericalDifferentation.o: numericalDifferentation.c 
	cc -c numericalDifferentation.c
clean:
	rm -rf *.o
	rm -rf main