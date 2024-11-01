#include <iostream>

using namespace std;

void PrintArr(int arr[], int arr_len)
{
    for(int i=0; i < arr_len; i++)
    {
        cout << arr[i] << " ";
    }
    cout << "\n\n";
}

void insert(int idx, int num, int arr[], int &arr_len)
{
    for(int i=arr_len; i > idx; i--)
    {
        // cout << i << endl;
        arr[i] = arr[i-1];
    }
    arr[idx] = num;
    arr_len++;
}

void erase(int idx, int arr[], int &arr_len)
{
    arr_len--;
    for(int i=idx; i < arr_len; i++)
    {
        arr[i] = arr[i+1];
    }
}

int main()
{
    int arr1[5] = {1, 3, 5};
    int arr_len1 = 3;

    insert(1, 2, arr1, arr_len1);
    PrintArr(arr1, arr_len1);

    int arr2[5] = {1, 2, 4, 3, 4};
    int arr_len2 = 5;

    erase(2, arr2, arr_len2);
    PrintArr(arr2, arr_len2);


    return 0;
}