var input = require('fs').readFileSync('stdin', 'utf8');
var valores = input.split("\n").map(item=>parseInt(item));
var testes = valores.shift();

//Cria objeto para salvar os valores calculados
var fib = {};

function fibonacci(n){
	if (n===0 || n===1){
		return n;
	}else if(fib.hasOwnProperty(n)){
		return fib[n];
	} else{
		return fibonacci(n-1) + fibonacci(n-2);
	}
}

for (var t=0;t<testes;t++){
	//Se ainda não foi calculado, calcule
	if (!fib.hasOwnProperty(valores[t])){
		fib[valores[t]] = fibonacci(valores[t]);
	}
	console.log("Fib("+valores[t]+") = "+fib[valores[t]]);
}