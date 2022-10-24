#include <stdio.h>

float main (){
  
  double a, b, c, triangulo, circulo, trapezio, quadrado, retangulo, pi;
  pi = 3.14; //Assumindo pi com esse valor 
  
  scanf("%lf %lf %lf", &a, &b, &c);

  triangulo = (a*c)/2;
  circulo = pi*c*c;
  trapezio = ((a + b)*c)/2;
  quadrado = b*b;
  retangulo = a*b;

  printf("TRIANGULO: %.3f\n", triangulo);
  printf("CIRCULO: %.3f\n", circulo);
  printf("TRAPEZIO: %.3f\n", trapezio);
  printf("QUADRADO: %.3f\n", quadrado);
  printf("RETANGULO: %.3f\n", retangulo);

}
