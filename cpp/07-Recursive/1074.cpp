#include<iostream>

using namespace std;

int func(int n, int r, int c)
{
    if (n == 0)
        return 0;

    int h = 1 << (n-1);
    if(r < h && c < h)
        return func(n-1, r, c);
    
    else if(r < h && c >= h)
        return h * h + func(n-1, r, (c - h));
    
    else if(r >= h && c < h)
        return 2 * h * h + func(n-1, (r - h), c);

    else
        return 3 * h * h + func(n-1, (r - h), (c - h));
}

int main()
{
    int N, R, C;
    cin >> N >> R >> C;

    int result = func(N, R, C);
    cout << result;
}