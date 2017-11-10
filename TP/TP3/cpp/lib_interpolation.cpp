#include "lib_interpolation.hpp"
#include <math.h>
#include <iostream>
#include <cstdlib>

using namespace std;

/* Distance Euclidienne entre deux points
 */
float distance(float p1x, float p1y, float p2x, float p2y)
{
	float x,y;
	x = p2x-p1x;
	y = p2y-p1y;
	return sqrt(x*x+y*y);
}

float di(int i, float x, float y, Xi *l)
{
	return distance(x,y,l[i].x,l[i].y);
}

float wi(int i, float x, float y, Xi *l, int N)
{
	float sum = 0;
	for(int j = 0; j < N; j++)
	{
		sum += (1/pow(di(j,x,y,l),l[j].mu));
	}
	return (1/pow(di(i,x,y,l),l[i].mu))/sum;
}

float F(float x, float y, Xi *l, int N)
{
	float res = 0;
	for(int i = 0; i < N; i++)
	{
		res += wi(i,x,y,l,N) * l[i].val;
	}
	return res;
}

void interpolation(int width, int height, Xi *l, int N){
	for(int x = 0; x < height; x++)
	{
		for(int y = 0; y < width; y++)
		{
			float f = F((float)x/(float)height,(float)y/(float)width,l,N);
			cout << (float)x/(float)height << " " << (float)y/(float)width << " " << " " << f << endl;
		}
	}
}

float cosSin(float x, float y) {
	return cos(x/2) + sin(y/2);
}

void generateRandomValues(float mu, Xi *l, int nb_gen, vFunctionCall f) {

	for(int i = 0; i<nb_gen; i++) {

		float pos_x = ((double) rand() / (RAND_MAX));
		float pos_y = ((double) rand() / (RAND_MAX));
		float val = f(pos_x, pos_y);
		l[i].x = pos_x;
		l[i].y = pos_y;
		l[i].y = val;
		l[i].mu = mu;

	}

}

void freet(float** t, int height){
	for(int i = 0; i < height; i++)
	{
		free(t[i]);
	}
	free(t);
}
