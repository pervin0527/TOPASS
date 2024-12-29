#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int a, b, c = 0;
    cin >> a;
    cin >> b;
    cin >> c;

    vector<int> arr(10, 0);
    int abc = a * b * c;
    while (true)
    {
        int quote = abc / 10;
        int remainder = abc % 10;
        arr[remainder] += 1;

        if (quote == 0)
            break;
        
        abc /= 10;
    }

    for(int i=0; i<10; i++)
    {
        cout << arr[i] << "\n";
    }

    return 0;
}