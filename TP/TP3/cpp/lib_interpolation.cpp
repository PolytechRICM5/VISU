#include "lib_interpolation.hpp"
#include <math.h>
#include <iostream>
#include <Eigen/Dense>
#include <cstdlib>

using namespace std;
using namespace Eigen;

/* 
 * Distance Euclidienne entre deux points
 */
float distance(float p1x, float p1y, float p2x, float p2y)
{
	float x,y;
	x = p2x-p1x;
	y = p2y-p1y;
	return sqrt(x*x+y*y);
}

/*
 * Distance au i-ème point de la liste.
 */
float di(int i, float x, float y, Xi *l)
{
	return distance(x,y,l[i].x,l[i].y);
}

/***********
 * SHEPARD *
 ***********/

float wi(int i, float x, float y, Xi *l, int N)
{
	float sum = 0;
	for(int j = 0; j < N; j++)
	{
		sum += (1/pow(di(j,x,y,l),l[j].mu));
	}
	return (1/pow(di(i,x,y,l),l[i].mu))/sum;
}

float F_shepard(float x, float y, Xi *l, int N)
{
	float res = 0;
	for(int i = 0; i < N; i++)
	{
		res += wi(i,x,y,l,N) * l[i].val;
	}
	return res;
}

void shepard(int width, int height, Xi *l, int N){
	for(int x = 0; x < height; x++)
	{
		for(int y = 0; y < width; y++)
		{
			float f = F_shepard((float)x/(float)height,(float)y/(float)width,l,N);
			cout << (float)x/(float)height << " " << (float)y/(float)width << " " << " " << f << endl;
		}
	}
}

/***********
 *  HARDY  *
 ***********/

float Hk(int k, float x, float y, Xi* l, float R)
{
	return sqrt(R + pow(di(k,x,y,l), 2));
}

float F_hardy(float x, float y, Xi *l, int N, float R, VectorXf alphas)
{
	float res = 0;
	for(int i = 0; i < N; i++)
	{
		res += alphas(i) * Hk(i,x,y,l,R);
	}
	return res;
}

VectorXf calculer_alphas(Xi *l, int N, float R)
{
	MatrixXf m(N,N);
	VectorXf v(N);
	for(int i = 0; i < N; i++)
	{
		for(int k = 0; k < N; k++)
		{
			m(i,k) = Hk(k, l[i].x, l[i].y, l, R);
		}
		v(i) = l[i].val;
	}
	VectorXf res = m.ldlt().solve(v);
	
	return res;
};

void hardy(int width, int height, Xi *l, int N, float R)
{
	VectorXf alphas = calculer_alphas(l, N, R);
	for(int x = 0; x < height; x++)
	{
		for(int y = 0; y < width; y++)
		{
			float f = F_hardy((float)x/(float)height,(float)y/(float)width,l,N,R,alphas);
			cout << (float)x/(float)height << " " << (float)y/(float)width << " " << " " << f << endl;
		}
	}
	cerr << "alphas : " << alphas << endl;
}

/**
 * Calculs de R 
 */

/*
 * Distance moyenne des points * 0.815
 */
float R_hardy(Xi *l, int N) {
	float d = 0;
	int steps = 0;
	for(int i = 0; i < N; i++)
	{
		float x = l[i].x;
		float y = l[i].y;
		for(int j = i+1; j < N; j++)
		{
			d += di(j,x,y,l);
			steps++;
		}
	}
	return 0.815 * d/steps;
}

/*
 * Diametre du cercle des données * 1.25 / sqrt(N)
 */
float R_franke(Xi *l, int N) {
	float diam = 0;
	for(int i = 0; i < N; i++)
	{
		float x = l[i].x;
		float y = l[i].y;
		for(int j = i+1; j < N; j++)
		{
			float d = di(j,x,y,l);
			if(d > diam) diam = d;
		}
	}
	return 1.25 * diam / sqrt(N);
}

/*
 * Constante de Stead
 */
 
float max(float a, float b) {
	if(a>b) return a;
	return b;
}

float R_stead(Xi *l, int N) {
	float mx = 0;
	float my = 0;
	float mz = 0;
	for(int i = 0; i < N; i++)
	{
		float x = l[i].x;
		float y = l[i].y;
		float z = l[i].val;
		for(int j = 0; j < N; j++)
		{
			mx = max(mx,x - l[j].x);
			my = max(my,y - l[j].y);
			mz = max(mz,z - l[j].val);
		}
	}
	return sqrt((1./10.) * max(max(mx,my),mz));
}

/**
 * GENERATION DE VALEURS
 */

float cosSin(float x, float y) {
	return cos(x/2) + sin(y/2);
}

void generateRandomValues(float mu, Xi *l, int nb_gen, vFunctionCall f) {
	
	srand(time(NULL));

	for(int i = 0; i<nb_gen; i++) {

		float pos_x = ((double) rand() / (RAND_MAX));
		float pos_y = ((double) rand() / (RAND_MAX));
		float val = f(pos_x, pos_y);
		l[i].x = pos_x;
		l[i].y = pos_y;
		l[i].y = val;
		l[i].mu = mu;
		
		cerr << pos_x << " " << pos_y << " " << val << endl;
	}

}
