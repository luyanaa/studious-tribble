$(pro)
main: testbench.o  findRoot.o
	cc -o main testbench.o findRoot.o
testbench.o: testbench.c findRoot.h
	cc -c testbench.c
numericalIntegral.o: findRoot.c 
	cc -c findRoot.c
clean:
	rm -rf *.o
	rm -rf main