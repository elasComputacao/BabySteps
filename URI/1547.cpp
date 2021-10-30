#include <iostream>

using namespace std;

int main(){

	int n;
	cin >> n;
	for (int i=0;i<n;i++){
		int qt,s;
		cin >> qt >> s;
		int guess[qt];

		for (int j=1;j<qt+1;j++){
			unsigned int z;
			cin >> z; 
			if(s>=z)
            	guess[j]=s-z;
            else
                guess[j]=z-s;
		}

		int win;
		int small=guess[1];
		for (int j=2;j<qt+1;j++){
			if(guess[j]<small)
				small=guess[j];
		}

		for (int j=1;j<qt+1;j++){
			if (small==guess[j]){
				win=j;
				break;
			}
		}

		cout << win << endl;
	}
	
	return 0;
}