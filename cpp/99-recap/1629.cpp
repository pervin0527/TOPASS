#include <iostream>

using namespace std;

long long func2(long long a, long long b, long long c)
{
    if (b == 1)
        return a % c;

    long long tmp = func2(a, b / 2, c);
    if (b % 2 == 0)
        return tmp * tmp % c;
    else
        return (tmp * tmp % c) * a % c;
}

long long func(long long a, long long b, long long c)
{
    if (b == 1)
        return a % c;

    long long tmp = func(a, b / 2, c);
    tmp = tmp * tmp % c;
    if (b % 2 == 0)
        return tmp;
    else
        return tmp * a % c;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long a, b, c;
    cin >> a >> b >> c;

    long long res = func2(a, b, c);
    cout << res;
}