#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    int offset = 1000000;
    int *arr = new int[2000001];
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        arr[num + offset]++;
    }

    for (int i = 0; i <= 2000000; i++)
    {
        while (arr[i] > 0)
        {
            cout << i - offset << "\n";
            arr[i]--;
        }
    }
}