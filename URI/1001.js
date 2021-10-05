const input = require("fs").readFileSync("./dev/stdin", "utf8");

let [A, B] = input.split("\n").map(item => parseInt(item));

let X = A + B;

console.log(`X = ${X}`);