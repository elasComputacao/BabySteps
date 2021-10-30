#include <iostream>
#include <math.h>

using namespace std;

int main(){

	int a,b,c;
	cin >> a >> b >> c;

	while (a!=0 || b!=0 || c!=0){
		cout << (int)pow(a*b*c,(1/3.0)) << endl;
		cin >> a >> b >> c;
	}

	return 0;
}