$(pro)
main: testbench.o  numericalIntegral.o
	cc -o main testbench.o numericalIntegral.o
testbench.o: testbench.c numericalIntegral.h
	cc -c testbench.c
numericalIntegral.o: numericalIntegral.c 
	cc -c numericalIntegral.c
clean:
	rm -rf *.o
	rm -rf main