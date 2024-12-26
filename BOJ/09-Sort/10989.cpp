#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    // 수의 범위: 1부터 10,000까지
    vector<int> freq(10001, 0);

    // 입력 값을 바로 카운팅
    for (int i = 0; i < n; i++)
    {
        int inp_num;
        cin >> inp_num;
        freq[inp_num]++;
    }

    // 카운팅 정렬 결과 출력
    for (int i = 1; i <= 10000; i++)
    {
        while (freq[i] > 0)
        {
            cout << i << "\n";
            freq[i]--;
        }
    }

    return 0;
}
