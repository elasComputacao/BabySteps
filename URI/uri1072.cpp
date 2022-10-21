#include <bits/stdc++.h>

using namespace std;

int main() {
    long long n, x;
    scanf("%lld", &n);
    long long result = 0;

    for (int i = 0; i < n; i++) {
        scanf("%lld", &x);

        if (x >= 10 && x <=20) result++;
    }

    printf("%lld in\n", result);
    printf("%lld out\n", (n - result));

    return 0;
}