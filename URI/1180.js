var input = require('fs').readFileSync('stdin', 'utf8');
var linhas = input.split("\n");
var tamanho = parseInt(linhas.shift());
var valores = linhas[0].split(" ").map(item=>parseInt(item)) ;

var min = valores[0];
var index = 0;
for (var i=0;i<valores.length;i++){
	if (valores[i]<min){
		min = valores[i];
		index = i;
	}
}

console.log("Menor valor: " + min);
console.log("Posicao: " + index)