import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
	
		Scanner input = new Scanner(System.in);
		
		float a = input.nextFloat();
		float b = input.nextFloat();
		float c = input.nextFloat();
		float d = input.nextFloat();
		
		float media = (a * 2 + b * 3 + c * 4 + d * 1) / 10;
		System.out.printf("Media: %.1f%n", media);
		
		if(media >= 7.0) {
			System.out.println("Aluno aprovado.");
		}
		else if(media < 5.0) {
			System.out.println("Aluno reprovado.");
		}
		else {
			System.out.println("Aluno em exame.");
			
			float notaExame = input.nextFloat();
			System.out.printf("Nota do exame: %.1f%n", notaExame);
			
			media = (media + notaExame) / 2;
			if(media >= 5.0) {
				System.out.println("Aluno aprovado.");
			}
			else {
				System.out.println("Aluno reprovado.");
			}
			
			System.out.printf("Media final: %.1f%n", media);
		}
		
		input.close();

	}
	
}
