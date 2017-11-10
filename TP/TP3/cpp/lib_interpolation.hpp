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


void interpolation(int width, int height, Xi *l, int N);

void freet(float** t, int height);
