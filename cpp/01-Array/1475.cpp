#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int room_number = 0;
    cin >> room_number;

    vector<int> arr(10, 0); // 0부터 9까지 각 숫자의 빈도 수 저장
    while (room_number > 0) {
        int remainder = room_number % 10;
        arr[remainder]++;
        room_number /= 10;
    }

    // 6과 9는 같은 세트를 공유
    arr[6] = (arr[6] + arr[9] + 1) / 2; // 반올림 처리
    arr[9] = 0; // 9는 더 이상 사용되지 않으므로 0으로 설정

    // 배열에서 최대값 찾기
    int max_n = 0;
    for (int i = 0; i < 10; i++) {
        if (arr[i] > max_n)
            max_n = arr[i];
    }

    cout << max_n << '\n';
    return 0;
}
