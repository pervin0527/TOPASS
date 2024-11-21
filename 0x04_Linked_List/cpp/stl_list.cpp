#include <iostream>
#include <list>

using namespace std;

int main()
{
    list<int> myList;

    // 맨 뒤에 원소 추가
    myList.push_back(10);
    myList.push_back(20);
    myList.push_back(30);

    // 맨 앞에 원소 추가
    myList.push_front(5);

    cout << "List elements: ";
    for (int elem : myList)
    {
        cout << elem << " ";
    }
    cout << endl;

    // 중간에 원소 삽입
    auto it = myList.begin();
    advance(it, 2); // 두 번째 위치로 이동
    myList.insert(it, 15); // 15를 삽입

    for (int elem : myList)
    {
        cout << elem << " ";
    }
    cout << endl;

    // 특정 원소 삭제
    auto it2 = myList.end();
    advance(it2, -2);
    myList.erase(it2);

    for (int elem : myList)
    {
        cout << elem << " ";
    }
    cout << endl;

    // 정렬
    myList.sort();

    cout << "After sorting: ";
    for (int elem : myList)
    {
        cout << elem << " ";
    }
    cout << endl;

    return 0;
}
