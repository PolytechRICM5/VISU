/* Autheurs : Aubertin Alicia & Bonhoure Gilles
 *
 * TP3 de VISU : Interpolation de données éparses
 */

#include <iostream>
#include <stdio.h>
#include "lib_interpolation.hpp"

using namespace std;

int main(int argc, char **argv)
{
	if(argc < 3){
		cout << "Donner les méthodes en paramètres.\n";
		exit(1);
	}
	
	int method = atoi(argv[1]);
	int method_R = atoi(argv[2]);
	
	int width = 100;
	int height = 100;
	
	
	
	float** res;
	int size = 3;
	Xi l[3];
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
	
	if(method ==1) {
		shepard(width, height, l, size);
	}
	if(method == 2) {
		float R = 0;
		if(method_R == 1) R = R_hardy(l,3);
		if(method_R == 2) R = R_franke(l,3);
		if(method_R == 3) R = R_stead(l,3);
		hardy(width, height, l, size,R);
	}

	return 0;
}
