// Questão 1008 resolvida com Javascript

const input = require("fs").readFileSync("./dev/stdin", "utf8");

let [number_func, horas, qtd_recebe_hora] = input.split("\n");

horas = parseInt(horas);
qtd_recebe_hora = parseFloat(qtd_recebe_hora);

const salario = horas * qtd_recebe_hora;

console.log(`NUMBER = ${number_func}\nSALARY = U$ ${salario.toFixed(2)}`);
