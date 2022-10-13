import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int i = 0;
        Scanner leitor = new Scanner(System.in);
        int n = leitor.nextInt();
        while (i<=n){
            if (i%2!=0){
                System.out.println(i);
            }
            i++;
        }
        
    }
    
}
