#include <iostream>
using namespace std;

int main()
{
    int room_number;
    cin >> room_number;

    int numbers[10] = {0};
    while (room_number > 0)
    {
        int num = room_number % 10;
        room_number /= 10;

        if (num == 6 || num == 9) {
            numbers[6]++;  // 6과 9는 같은 인덱스(6)를 사용
        } else {
            numbers[num]++;
        }
    }

    // 6과 9의 개수를 하나로 묶어 반올림
    numbers[6] = (numbers[6] + 1) / 2;

    // 배열에서 최대값 찾기
    int max_set = 0;
    for (int i = 0; i < 10; i++) {
        if (numbers[i] > max_set) {
            max_set = numbers[i];
        }
    }
    cout << max_set;

    return 0;
}
