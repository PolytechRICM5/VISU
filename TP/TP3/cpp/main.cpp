/* Autheurs : Aubertin Alicia & Bonhoure Gilles
 *
 * TP3 de VISU : Interpolation de données éparses
 */

#include <stdio.h>
#include "lib_interpolation.hpp"

int main(int argc, char **argv)
{
	float** res;
	Xi l[50];

	/*
	l[0].x = 0.5;
	l[0].y = 0.5;
	l[0].val = 5;
	l[0].mu = 2;
	l[1].x = 0.4;
	l[1].y = 0.2;
	l[1].val = 1;
	l[1].mu = 4;
	l[2].x = 0.8;
	l[2].y = 0.8;
	l[2].val = 2;
	l[2].mu = 2;
	*/

	generateRandomValues(1, l, 50, (vFunctionCall) cosSin);

	interpolation(100,100,l,3);

	return 0;
}
