#include <iostream>

using namespace std;

int func(int n)
{
    if (n == 1)
        return 1;

    return n + func(n-1);
}

int main()
{
    // 1부터 N까지의 합을 구하는 재귀함수.
    
    int n;
    cin >> n;

    int result = func(n);
    cout << result << "\n";
}