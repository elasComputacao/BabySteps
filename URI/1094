using System; 

class URI {

    static void Main(string[] args) { 

         string[] lista1;
            int rep = 0;
            int N = Convert.ToInt32(Console.ReadLine());
            double c = 0;
            double r = 0;                               //se for dividir int por int da int
            double s = 0; 
           
            while (rep < N)
            {
                lista1 = (Console.ReadLine()).Split(' ');
                int x = Convert.ToInt32(lista1[0]);
                string T = (lista1[1]);
                if (T == "C")
                {
                    c += x;               
                }
                if (T == "R")
                {
                    r += x;               
                }
                if (T == "S")
                {
                    s += x;                  
                }
                rep++;

               

            }
            double cobaias = s + r + c;
            double pc = (c * 100) / cobaias;
            double pr = (r * 100) / cobaias;
            double ps = (s * 100) /cobaias;
            
            Console.WriteLine("Total: {0} cobaias", cobaias);
            Console.WriteLine("Total de coelhos: {0}", c);
            Console.WriteLine("Total de ratos: {0}", r);
            Console.WriteLine("Total de sapos: {0}",s);
            Console.WriteLine("Percentual de coelhos: {0:0.00} %", pc);
            Console.WriteLine("Percentual de ratos: {0:0.00} %", pr);
            Console.WriteLine("Percentual de sapos: {0:0.00} %", ps);

    }

}
