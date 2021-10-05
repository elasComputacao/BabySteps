#include <iomanip>
#include <iostream>
 
using namespace std;
 
int main() {
    int a, b;
    float c;
    cin >> a >> b >> c;
    cout << "NUMBER = " << a << endl;
    cout << setprecision(2) << fixed;
    cout << "SALARY = U$ " << b*c << endl;
}