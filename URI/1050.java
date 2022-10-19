import java.io.IOException;
import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
 
    Scanner sc = new Scanner(System.in);
    int ddd[] = {61, 71, 11, 21, 32, 19, 27, 31};
    String cidades[] = {"Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro", "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte"};
    
    int entrada = sc.nextInt();
    int i, j = 0;
    
    for (i = 0; i < 8; i++) {
        if (entrada == ddd[i]) {
            System.out.println(cidades[i]);
        } else {
            j++;
        }
    }
    if (i == j) {
        System.out.printf("DDD nao cadastrado\n");
    }
 
  }
}
