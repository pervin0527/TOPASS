#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int a[5] = {1, 4, 5, 2, 7};
    
    // sort() 함수는 [시작, 끝) 형태의 반개구간을 사용합니다.(파이썬의 슬라이싱처럼 시작은 포함하나 끝은 포함하지 않음.)
    // 따라서 a+5는 마지막 원소 다음을 가리키며, 실제로는 a[0]~a[4]까지만 정렬됩니다.
    sort(a, a+5);

    for(int i = 0; i < 5; i++)
        cout << a[i] << " ";
    cout << '\n';

    vector<int> v = {1, 4, 5, 2, 7};
    sort(v.begin(), v.end());

    for(int i = 0; i < 5; i++)
        cout << v[i] << " ";
    cout << '\n';
}