#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> arr(n, 0);
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    /* vector를 오름차순으로 정렬하고 역순으로 출력하는 방식. */
    // sort(arr.begin(), arr.end());
    // for (int i = n - 1; i >= 0; i--)
    //     cout << arr[i] << "\n";

    /* vector를 내림차순으로 정렬하고 그대로 출력하는 방식*/
    // reverse(arr.begin(), arr.end()); // reverse는 그냥 벡터의 순서를 역으로 뒤집는 것이기 때문에 내림차순 정렬이 아님.
    // greater<int> : 두 값을 비교하여 첫 번째 값이 두 번째 값보다 크면 true를 반환하여 큰 값이 앞쪽(왼쪽)에 위치하도록 한다.
    sort(arr.begin(), arr.end(), greater<int>());

    for (int i = 0; i < n; i++)
        cout << arr[i] << "\n";
}