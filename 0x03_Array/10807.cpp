#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N;
    int v;
    int arr[201] = {0};
    
    cin >> N;
    for (int i=0; i<N; i++)
    {
        int number = 0;
        cin >> number;
        arr[100 + number] += 1;
    }
    cin >> v;

    cout << arr[100 + v] << endl;

    return 0;
}