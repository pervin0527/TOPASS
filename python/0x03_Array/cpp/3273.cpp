#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<int> numbers(n, 0);
    int max_item = 0;

    // 입력값을 받아 numbers 배열에 저장하고 max_item 갱신
    for (int i = 0; i < n; i++)
    {
        cin >> numbers[i];
        if (numbers[i] > max_item)
        {
            max_item = numbers[i];
        }
    }

    int x;
    cin >> x;

    // check_arr를 max_item에 따라 크기 설정
    vector<pair<bool, int> > check_arr(max_item + 1, make_pair(false, -1));

    // check_list에 값을 저장
    for (int i = 0; i < n; i++)
    {
        check_arr[numbers[i]] = make_pair(true, i);
    }

    int counter = 0;
    for (int i = 0; i < n; i++)
    {
        int v1 = numbers[i];
        int v2 = x - v1;

        // v2가 유효한 범위인지 확인하고 조건을 만족하는지 확인
        if (v2 > 0 && v2 <= max_item && check_arr[v2].first == true && check_arr[v2].second > i)
        {
            counter += 1;
        }
    }

    cout << counter;
    return 0;
}
