#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int main()

{
    int a, b;
    cin >> a >> b;

    long long count = 0;

    for (int x = fmin(a, b) + 1; x < fmax(a, b); x++)
    {
        if (x % 2)
        {
        count += x;
        }
    }
    cout << count << endl;
}