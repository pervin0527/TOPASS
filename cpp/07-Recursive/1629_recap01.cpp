#include <iostream>

using namespace std;

long long func(long long a, long long b, long long c)
{
    // base condition
    if(b == 1)
        return a % c;

    long long tmp = func(a, b/2, c); // a^b 부터 a^1까지 차례대로 함수를 재귀호출한다.

    // base condition인 a^1 에서부터 return을 시작해 결과들을 bottom-up으로 구하면 (a^b) % c를 구하게 된다.
    if (b % 2 == 0)
        return (tmp * tmp) % c;
    else
        return (tmp * tmp * a) % c;
}

int main()
{
    long long a, b, c;
    cin >> a >> b >> c;

    cout << func(a, b, c);
}