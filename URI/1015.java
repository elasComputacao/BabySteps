import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		double x1 = input.nextDouble();
		double y1 = input.nextDouble();
		
		double x2 = input.nextDouble();
		double y2 = input.nextDouble();
		
		double distancia = calculaDistanciaEntrePontos(x1, y1, x2, y2);
		
		System.out.printf("%.4f%n", distancia);
        
		input.close();
	}
	
	public static double calculaDistanciaEntrePontos(double x1, double y1, double x2, double y2) {
		return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
	}

}
