#include <iostream>
#include <list>

using namespace std;

int main()
{
    list<int> lst;

    // 요소 삽입
    lst.insert(lst.begin(), 10); // 인덱스 0에 10 삽입
    lst.insert(next(lst.begin(), 1), 20); // 인덱스 1에 20 삽입
    lst.insert(next(lst.begin(), 2), 30); // 인덱스 2에 30 삽입

    // 리스트 출력
    for (int value : lst)
    {
        cout << value << " ";
    }
    cout << "\n\n";

    // 요소 삽입
    lst.insert(lst.begin(), 7); // 인덱스 0에 7 삽입
    for (int value : lst)
    {
        cout << value << " ";
    }
    cout << "\n\n";

    // 요소 삽입
    lst.insert(next(lst.begin(), 2), 17); // 인덱스 2에 17 삽입
    for (int value : lst)
    {
        cout << value << " ";
    }
    cout << "\n\n";

    // 요소 삽입
    lst.insert(next(lst.begin(), 4), 40); // 인덱스 4에 40 삽입
    for (int value : lst)
    {
        cout << value << " ";
    }
    cout << "\n\n";

    // 요소 삭제
    lst.erase(lst.begin()); // 인덱스 0 삭제
    for (int value : lst)
    {
        cout << value << " ";
    }
    cout << "\n\n";

    // 요소 삭제
    lst.erase(next(lst.begin(), 3)); // 인덱스 3 삭제
    for (int value : lst)
    {
        cout << value << " ";
    }
    cout << "\n\n";

    // 요소 삭제
    lst.erase(next(lst.begin(), 1)); // 인덱스 1 삭제
    for (int value : lst)
    {
        cout << value << " ";
    }
    cout << "\n\n";

    // prev를 사용하여 end()에서 한 칸 뒤로 이동 (마지막 요소로 이동)
    lst.erase(prev(lst.end(), 1)); // lst.end()에서 한 칸 뒤로 이동
    for (int value : lst)
    {
        cout << value << " ";
    }
    cout << "\n\n";

    return 0;
}
