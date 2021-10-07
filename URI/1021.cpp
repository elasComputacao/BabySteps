#include <cstdio>


int main() {
        double d;
        scanf("%lf", &d);

        printf("NOTAS:\n");

        printf("%d nota(s) de R$ 100.00\n", int(d)/100);

        d -= (int(d)/100) * 100;

        printf("%d nota(s) de R$ 50.00\n", int(d)/50);

        d -= (int(d)/50) * 50;

        printf("%d nota(s) de R$ 20.00\n", int(d)/20);

        d -= (int(d)/20) * 20;

        printf("%d nota(s) de R$ 10.00\n", int(d)/10);

        d -= (int(d)/10) * 10;

        printf("%d nota(s) de R$ 5.00\n", int(d)/5);

        d -= (int(d)/5) * 5;

        printf("%d nota(s) de R$ 2.00\n", int(d)/2);

        d -= (int(d)/2) * 2;

        printf("MOEDAS:\n");

        printf("%d moeda(s) de R$ 1.00\n", int(d));

        d -= int(d);

        d *= 100;

        printf("%d moeda(s) de R$ 0.50\n", int(d)/50);

        d -= (int(d)/50) * 50;

        printf("%d moeda(s) de R$ 0.25\n", int(d)/25);

        d -= (int(d)/25) * 25;

        printf("%d moeda(s) de R$ 0.10\n", int(d)/10);

        d -= (int(d)/10) * 10;

        printf("%d moeda(s) de R$ 0.05\n", int(d)/5);

        d -= (int(d)/5) * 5;

        printf("%d moeda(s) de R$ 0.01\n", int(d));

        return 0;

}
