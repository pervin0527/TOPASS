#include <iostream>

using namespace std;

int main()
{
    int a, b, c;
    cin >> a;
    cin >> b;
    cin >> c;

    int abc = a * b * c;
    int counter[10] = {0};
    while (abc != 0)
    {
        int remain = abc % 10;
        counter[remain] += 1;
        abc = abc / 10;
    }

    for(int i=0; i<10; i++)
    {
        cout << counter[i] << endl;
    }
    return 0;
}