#include <iostream>

using namespace std;

void PrintArr(int &arr_len, int arr[])
{
    for(int i=0; i<arr_len; i++)
    {
        cout << arr[i] << " ";
    }
    cout << "\n";
}

void insert(int idx, int value, int &arr_len, int arr[])
{
    for(int i = arr_len; i > idx; i--)
    {
        arr[i] = arr[i-1];
    }
    arr[idx] = value;
    arr_len++;
}

void pop(int idx, int &arr_len, int arr[])
{
    for(int i = idx; i < arr_len; i++)
    {   
        arr[i] = arr[i+1];
    }
    arr_len--;
}

int main()
{
    int arr[10] = {10, 20, 30, 40, 50, 60};
    int arr_len = 6;

    cout << "insert" << endl;
    insert(1, 17, arr_len, arr);
    PrintArr(arr_len, arr);

    cout << "\npop" << endl;
    pop(1, arr_len, arr);
    PrintArr(arr_len, arr);

    return 0;
}