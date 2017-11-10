
all: lib_interpolation.o main.cpp
	g++ -o main main.cpp lib_interpolation.o -lm

lib_interpolation.o: lib_interpolation.hpp lib_interpolation.cpp
	g++ -I ../Eigen -c lib_interpolation.cpp -lm
