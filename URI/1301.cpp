
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include <ctime>
 
#define Inf 2147483647
#define Pi acos(-1.0)
#define N 1000000
#define M 100000
#define LL long long
 
inline LL Power(int b, int p) { LL ret = 1; for ( int i = 1; i <= p; i++ ) ret *= b; return ret; }
 
#define F(i, a, b) for( int i = (a); i < (b); i++ )
#define Fs(i, sz) for( size_t i = 0; i < sz.size (); i++ )
#define Fe(i, x) for(typeof (x.begin()) i = x.begin(); i != x.end (); i++)
#define Set(a, s) memset(a, s, sizeof (a))
#define max(a, b)  (a < b ? b : a)
#define min(a, b)  (a > b ? b : a)
 
using namespace std;
 
int x [M + 10];
int segTree [4 * M + 100];
 
void buildTree (int at, int lo, int hi)
{
    if ( lo == hi ) {
        segTree [at] = x [lo];
        return;
    }
 
    int mid = (lo + hi) / 2;
 
    buildTree(2 * at, lo, mid);
    buildTree(2 * at + 1, mid + 1, hi);
 
    segTree [at] = segTree [2 * at] * segTree [2 * at + 1];
}
 
void update (int at, int index, int value, int lo, int hi)
{
    if ( index < lo || index > hi ) return;
 
    if ( lo == hi ) {
        segTree [at] = value;
        return;
    }
 
    int mid = (lo + hi) / 2;
 
    update(2 * at, index, value, lo, mid);
    update(2 * at + 1, index, value, mid + 1, hi);
 
    segTree [at] = segTree [2 * at] * segTree [2 * at + 1];
}
 
int query (int at, int lo, int hi, int start, int endInd)
{
    if ( start > hi || endInd < lo ) return 1;
 
    if ( lo >= start && hi <= endInd ) return segTree [at];
 
    int mid = (lo + hi) / 2;
 
    return query (2 * at, lo, mid, start, endInd) * query (2 * at + 1, mid + 1, hi, start, endInd);
}
 
void print()
{
    printf ("\n... printing start... \n");
    F(i, 0, 4 * M) {
        printf (" %d", segTree [i]);
    }
    printf ("\n... printing end... \n");
}
 
int main ()
{
    int n, k;
 
    while ( scanf ("%d %d", &n, &k) != EOF ) {
 
        F(i, 0, n) {
            scanf ("%d", &x [i]);
 
            if ( x [i] > 1 ) x [i] = 1;
            if ( x [i] < -1 ) x [i] = -1;
        }
 
        buildTree(1, 0, n - 1);
        //print();
 
        char cmd [5];
 
        while ( k-- ) {
            scanf ("%s", cmd);
 
            if ( cmd [0] == 'C') {
                int ind, val; scanf ("%d %d", &ind, &val);
                ind--;
 
                if ( val > 1 ) val = 1;
                if ( val < -1 ) val = -1;
 
                update(1, ind, val, 0, n - 1);
                //print();
 
                x [ind] = val;
 
            } else {
                int start, endInd; scanf ("%d %d", &start, &endInd);
                start--;
                endInd--;
 
                int res = query(1, 0, n - 1, start, endInd);
 
                if ( res == 1 ) printf ("+");
                else if ( res == -1 ) printf ("-");
                else printf ("0");
 
            }
        }
 
        printf ("\n");
    }
 
    return 0;
}
 