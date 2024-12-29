#include <iostream>
using namespace std;

long long func(long long a, long long b, long long c) {
    if(b == 1)
        return a % c;
        
    long long temp = func(a, b/2, c);
    
    if(b % 2 == 0)
        return (temp * temp) % c;
    else
        return ((temp * temp) % c * a) % c;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    long long A, B, C;
    cin >> A >> B >> C;
    
    cout << func(A, B, C);
    return 0;
}