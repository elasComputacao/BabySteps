#include <iostream>

using namespace std;

int main(){

	int n,x,y,sum=0;
	cin >> n;

	for (int i=0;i<n;i++){
		cin >> x >> y;

		//par
		if (x%2==0){

			for (int j=1;j<y*2;j+=2)
				sum+=x+j;

			cout << sum << endl;
		}

		//impar
		else{

			for (int j=0;j<y*2;j+=2)
				sum+=x+j;

			cout << sum << endl;	
			
		}

		sum=0;
	}

	return 0;
}