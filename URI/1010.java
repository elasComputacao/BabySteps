import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
 
      Scanner sc = new Scanner(System.in);
      int c1, c2, n1, n2;
      double v1, v2, total;
      
      c1 = sc.nextInt();
      n1 = sc.nextInt();
      v1 = sc.nextDouble();
      c2 = sc.nextInt();
      n2 = sc.nextInt();
      v2 = sc.nextDouble();
      
      total = (n1 * v1) + (n2 * v2);
      System.out.format("VALOR A PAGAR: R$ %.2f\n", total);
    }
}
