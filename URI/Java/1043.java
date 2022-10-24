import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		double a = input.nextDouble();
		double b = input.nextDouble();
		double c = input.nextDouble();
		
		if(isTriangulo(a, b, c)) {
			//Perímetro do triângulo
			double perimetro = a + b + c;
			System.out.printf("Perimetro = %.1f%n", perimetro);
		}
		else {
			//Área do trapézio
			double area = ((a + b) * c) / 2;
			System.out.printf("Area = %.1f%n", area);
		}

	}
	
	
	public static boolean isTriangulo (double a, double b, double c) {
		if(Math.abs(b - c) < a && a < b + c) {
			if(Math.abs(a - c) < b && b < a + c) {
				if(Math.abs(a - b) < c && c < a + b) {
					return true;
				}
			}
		}
		return false;
	}

}
