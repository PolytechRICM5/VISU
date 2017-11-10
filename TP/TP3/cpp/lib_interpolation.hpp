#include <stdio.h>
#include <stdlib.h>


typedef struct xi {
	float x;
	float y;
	float val;
	float mu;
} Xi;


typedef struct point {
	float x;
	float y;
} Point;

typedef float (* vFunctionCall)(float x, float y);

float cosSin(float x, float y);

void interpolation(int width, int height, Xi *l, int N);

void generateRandomValues(float mu, Xi *l, int nb_gen, vFunctionCall f);

void freet(float** t, int height);
