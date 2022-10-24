import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);
        int num = leitor.nextInt();
        int fatorial = fatorial(num);
        System.out.println(fatorial);
    }
    static int fatorial(int n) {
        if (n<=1){
            return 1;
        } else {
            return n*fatorial(n-1);
        }
    }
}
