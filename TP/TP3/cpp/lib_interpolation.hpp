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


void shepard(int width, int height, Xi *l, int N);
void hardy(int width, int height, Xi *l, int N, float R);

float R_hardy(Xi *l, int N);
float R_franke(Xi *l, int N);
float R_stead(Xi *l, int N);

