#include <iostream>

using namespace std;

int main(){

	int integrantes; // min=2 max=10^4
	int compassos, soma, media, iguais;
	int i;

	while (cin >> integrantes){
		//reset
		compassos=1;
		soma=0;
		iguais=0;
		//read
		int nota[integrantes];
		for (i=0;i<integrantes;i++){
			cin >> nota[i];
			soma+=nota[i];
		}
		media=soma/integrantes;

		for (i=0;i<integrantes;i++)
			iguais += media-nota[i];

		if (iguais!=0)
			cout << "-1" << endl;
		else{
			//compassos igual a soma de todos os numeros
			//maiores que a media menos a media
			for (i=0;i<integrantes;i++){
				if (nota[i]>media)
					compassos+=nota[i]-media;
			}
			
			cout << compassos << endl;
		}	
	}

	return 0;
}