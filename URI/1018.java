//Questão 1018

import java.io.IOException;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int valor = sc.nextInt();
    System.out.println(valor);
    int[] notas = {100, 50, 20, 10, 5, 2, 1};

    for(int nota: notas){
      int quantidade = valor/nota;
      System.out.printf("%d nota(s) de R$ %d,00\n", quantidade, nota);
      valor -= quantidade * nota;
    }

  }
}
