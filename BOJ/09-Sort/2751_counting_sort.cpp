#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    const int OFFSET = 1'000'000;       // 음수 처리용 offset
    const int MAX_VAL = 2 * OFFSET + 1; // freq 배열 크기

    int *freq = new int[MAX_VAL](); // 초기화 포함 배열 생성

    // 입력과 freq 배열 업데이트
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        freq[num + OFFSET]++; // 음수와 양수 모두 처리
    }

    // 정렬된 결과 출력
    for (int i = 0; i < MAX_VAL; i++)
    {
        while (freq[i] > 0) // 빈도만큼 출력
        {
            cout << (i - OFFSET) << "\n";
            freq[i]--;
        }
    }

    delete[] freq; // 동적 메모리 해제
    return 0;
}
