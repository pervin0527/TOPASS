#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    int offset = 1000000;
    int *arr = new int[2000001](); // ()을 추가하면 모든 원소를 0으로 초기화.
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        int new_idx = offset + num; // counting sort에서 배열의 인덱스는 특정 숫자. 0이 배열의 중앙이고 offset을 더해 음수와 양수를 표현할 수 있게함.
        arr[new_idx]++;             // 배열의 idx번째에 저장된 값은 idx가 등장한 횟수.
    }

    for (int i = 0; i < 2000000; i++) // idx가 몇 번 등장했는지.
    {
        while (arr[i] > 0)
        {
            cout << i - offset << "\n";
            arr[i]--;
        }
    }
}