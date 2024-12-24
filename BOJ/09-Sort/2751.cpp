#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    /* 배열을 사용한 풀이*/
    // int *arr = new int[n];
    // for(int i = 0; i < n; i++)
    //     cin >> arr[i];

    // sort(arr, arr + n);
    // for(int i = 0; i < n; i++)
    //     cout << arr[i] << "\n";

    /* STL vector를 사용한 풀이 */
    vector<int> arr(n, 0);
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    sort(arr.begin(), arr.end());
    for (int i = 0; i < n; i++)
        cout << arr[i] << "\n";
}