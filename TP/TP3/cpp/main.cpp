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
	int size = 50;
	Xi l[50];
	generateRandomValues(1, l, 50, (vFunctionCall) cosSin);
	
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
