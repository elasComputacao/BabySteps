var valor = lines[0];
const array = [100, 50, 20, 10, 5, 2, 1];

console.log(valor);
array.forEach(e => {
  const nota = Math.trunc(valor/e);
  valor = Number(valor) - e * nota;
  console.log(nota + " nota(s) de R$ " + e + ",00");
});
