using System; 

class URI {

    static void Main(string[] args) { 

        string SM = Console.ReadLine();
            double soma = 0;
            double[,] matriz = new double[12, 12];
            double num = 0;
            int M = 0;
            for (int linha = 0; linha < 12; linha++)
            {
                for (int coluna = 0; coluna < 12; coluna++)
                {
                    num = Convert.ToDouble(Console.ReadLine());
                    matriz[linha, coluna] = num;

                    if (linha > 11 - coluna)
                    {
                        soma += matriz[linha, coluna];
                        M++;
                    }
                }
            }
            
            if (SM == "S")
            {
                Console.WriteLine("{0:0.0}", soma);
            }
            if (SM == "M")
            {
                Console.WriteLine("{0:0.0}", soma / M);
            }


    }

}
