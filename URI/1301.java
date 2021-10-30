import java.io.IOException;
import java.util.Scanner;

public class Main {

	static int[] as = new int[4000010];
	static int[] z = new int[1000010];

	static int valor(int a) {
		if (a > 0)
			return 1;
		else {
			if (a < 0)
				return -1;
			else
				return 0;
		}
	}

	static void constroi(int indice, int e1, int e2) {
		if (e1 == e2)
			as[indice] = valor(z[e1 - 1]);
		else {
			int m = (e2 + e1) / 2;
			constroi(2 * indice, e1, m);
			constroi(2 * indice + 1, m + 1, e2);
			as[indice] = as[indice * 2] * as[indice * 2 + 1];
		}
	}

	static void atualiza(int indice, int e1, int e2, int i, int x) {
		if (i > e2 || i < e1)
			return;
		if (e1 == e2 && e2 == i) {
			as[indice] = valor(x);
			return;
		}

		int m = (e1 + e2) / 2;
		atualiza(2 * indice, e1, m, i, x);
		atualiza(2 * indice + 1, m + 1, e2, i, x);
		as[indice] = as[indice * 2] * as[indice * 2 + 1];
	}

	static int consulta(int indice, int e1, int e2, int i, int j) {
		if (i > e2 || j < e1)
			return 1;

		if (e1 >= i && e2 <= j)
			return as[indice];

		int m = (e1 + e2) / 2;
		int x = consulta(indice * 2, e1, m, i, j);
		int y = consulta(indice * 2 + 1, m + 1, e2, i, j);

		return x * y;
	}

	public static void main(String[] args) throws IOException {
		Scanner input = new Scanner(System.in);
		while (input.hasNext()) {
			int n = input.nextInt();
			int k = input.nextInt();
			for (int i = 0; i < n; i++) {
				z[i] = input.nextInt();
			}

			constroi(1, 1, n);
			for (int i = 0; i < k; i++) {
				String c = input.next();
				int e1 = input.nextInt();
				int e2 = input.nextInt();
				if (c.equals("P")) {
					int r = consulta(1, 1, n, e1, e2);
					if (r == 1)
						System.out.print("+");
					else {
						if (r == 0)
							System.out.print("0");
						else
							System.out.print("-");
					}
				} else if (c.equals("C"))
					atualiza(1, 1, n, e1, e2);
			}
			System.out.println();
		}
	}

}