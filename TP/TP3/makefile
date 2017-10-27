
all: lib_interpolation.o main.c
	gcc -o main main.c lib_interpolation.o -lm

lib_interpolation.o: lib_interpolation.h lib_interpolation.c
	gcc -c lib_interpolation.c -lm
