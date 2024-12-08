#include <iostream>
#include <vector>

using namespace std;

void func(int n, int m, int idx, vector<int>& arr, vector<bool>& check)
{
    if(arr.size() == m)
    {
        for(const auto elem : arr)
            cout << elem << " ";
        cout << "\n";
    }

    for(int i = 1; i < (n+1); i++)
    {
        // 중복 없는 수열
        if(check[i-1] == 1)
            continue;

        // 오름차순을 만들기 위해 이전에 채운 칸과 현재 채울 값을 비교.
        if(arr.size() > 0 && arr[idx-1] > i)
            continue;

        arr.push_back(i);
        check[i-1] = 1;
        func(n, m, idx+1, arr, check);
        arr.pop_back();
        check[i-1] = 0;
    }
}


int main()
{
    int n, m;
    cin >> n >> m;

    vector <int> arr; // 수열
    vector <bool> check(n, 0); // 선택 여부 확인용

    func(n, m, 0, arr, check);
}