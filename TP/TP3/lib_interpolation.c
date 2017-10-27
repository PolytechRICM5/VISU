#include "lib_interpolation.h"
#include <math.h>

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

float** interpolation(int width, int height, Xi *l, int N){
	float** res = malloc(height * sizeof(float*));
	for(int i = 0; i < height; i++)
	{
		res[i] = malloc(width * sizeof(float));
	}
	for(int x = 0; x < height; x++)
	{
		for(int y = 0; y < width; y++)
		{
			float f = F((float)x/(float)height,(float)y/(float)width,l,N);
			printf("%f\t%f\t%f\n",(float)x/(float)height,(float)y/(float)width,f);
			res[x][y] = f;
		}
	}
	
	return res;
}

void freet(float** t, int height){
	for(int i = 0; i < height; i++)
	{
		free(t[i]);
	}
	free(t);
}


