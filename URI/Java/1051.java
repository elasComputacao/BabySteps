import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		double imposto = 0.00;		
		double salario = input.nextDouble();
		
		if(2000.00 < salario && salario <= 3000.00) {
			imposto += calculaImposto(salario - 2000.00, 8);
		}
		else if(3000.00 < salario && salario <= 4500.00) {
			imposto += calculaImposto(1000.00, 8);
			imposto += calculaImposto(salario - 3000.00, 18);
		}
		else if(4500.00 < salario) {
			imposto += calculaImposto(1000.00, 8);
			imposto += calculaImposto(1500.00, 18);
			imposto += calculaImposto(salario - 4500.00, 28);
		}
		
		
		if(imposto == 0.00) {
			System.out.println("Isento");
		}
		else {
			System.out.printf("R$ %.2f%n", imposto);
		}
		
		input.close();
	}
	
	
	public static double calculaImposto(double valor, int taxa) {
		return valor * taxa / 100;
	}

}
