#include <iostream>
#include <vector>

using namespace std;

void func(int n, int m, vector<int> arr, vector<bool> chosen)
{
    if(arr.size() == m)
    {
        for(const auto item : arr)
            cout << item << " ";
        cout << "\n";

        return;
    }

    for(int i = 1; i <= n; i++)
    {
        if (chosen[i-1] != 1)
        {
            arr.push_back(i);
            chosen[i-1] = 1; // i가 선택되었음을 표시.
            func(n, m, arr, chosen); // i가 선택된 상태로 다음 숫자를 선택하기 위한 재귀호출.

            arr.pop_back(); // i를 제거하고 선택되지 않은 상태로 되돌아감 -> 다음 숫자를 선택하기 위함.
            chosen[i-1] = 0;
        }

    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, M;
    cin >> N >> M;

    vector<int> arr;
    vector<bool> chosen(N, 0);

    func(N, M, arr, chosen);
}