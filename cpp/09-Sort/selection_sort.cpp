#include <iostream>

using namespace std;

int main()
{
    int arr[10] = {3, 2, 7, 116, 62, 235, 1, 23, 55, 77};
    
    for(int i = 0; i < 10-1; i++)
    {
        int min_idx = i;
        for(int j = i+1; j < 10; j++)
        {
            if(arr[min_idx] > arr[j])
                min_idx = j;
        }
        int tmp = arr[i];
        arr[i] = arr[min_idx];
        arr[min_idx] = tmp;

        for(int k = 0; k < 10; k++)
            cout << arr[k] << " ";
        cout << "\n";
    }
}