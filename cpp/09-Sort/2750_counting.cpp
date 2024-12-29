#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    // 범위: -1000 ~ 1000
    int offset = 1000; // 음수를 처리하기 위한 offset
    int *freq = new int[2001](); // -1000 ~ 1000을 0 ~ 2000에 매핑

    // 입력 및 빈도 계산
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        freq[num + offset]++;
    }

    // 정렬 결과 출력
    for (int i = 0; i <= 2000; i++) // 전체 범위 탐색
    {
        if (freq[i] > 0) // freq[i]가 0보다 크면 출력
        {
            cout << i - offset << '\n'; // offset을 다시 빼서 원래 값 복원
        }
    }

    // 동적 메모리 해제
    delete[] freq;

    return 0;
}
