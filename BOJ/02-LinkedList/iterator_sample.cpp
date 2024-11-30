#include <iostream>
#include <list>

using namespace std;

void PrintLinkedList(const list<int> &ll)
{
    for(const auto item : ll)
        cout << item << " ";
    cout << "\n";
}

// template<typename T>
// void PrintLinkedList(const list<T> &ll)
// {
//     for(const auto &item : ll)
//         cout << item;
// }

int main()
{
    list<int> ll;
    for(int i = 0; i < 10; i++)
    {
        ll.push_back(i * 10);
    }

    // 원소를 순회하면서 값을 변경하지 않는 경우 const를 사용한다.
    PrintLinkedList(ll); // 0 10 20 30 40 50 60 70 80 90

    ll.insert(ll.begin(), 17); // 맨 앞에 17을 삽입한다.
    PrintLinkedList(ll); // 17 0 10 20 30 40 50 60 70 80 90

    ll.insert(next(ll.begin(), 2), 7); // 인덱스 2에 7을 삽입.
    PrintLinkedList(ll);

    ll.insert(ll.end(), 1000); // 마지막에 1000을 삽입.
    PrintLinkedList(ll); // 17 0 7 10 20 30 40 50 60 70 80 90 1000

    ll.insert(prev(ll.end(), 3), 99);
    PrintLinkedList(ll); // 17 0 7 10 20 30 40 50 60 70 99 80 90 1000

    // ll.end()는 리스트의 끝 이후를 나타내는 반복자이므로, erase 함수에 전달해서는 안된다.
    list<int>::iterator itr1 = prev(ll.end());
    itr1 = ll.erase(itr1); // 마지막 원소 삭제 후, 다음 원소를 가리키는 반복자를 반환함.
    PrintLinkedList(ll); // 17 0 7 10 20 30 40 50 60 70 99 80 90
    
    --itr1; // 마지막 원소 삭제 후, 다음 원소를 가리키는 반복자를 반환함. 따라서 다시 왼쪽으로 한칸 이동시켜야 마지막 원소에 해당.
    cout << "현재 가리키는 원소: " << *itr1 << endl;

    itr1 = prev(ll.end()); // 초기화
    cout << "마지막 원소: " << *itr1 << endl;

    list<int>::iterator itr2 = ll.begin();
    cout << *itr2 << endl;
    
    itr2 = ll.erase(itr2);
    PrintLinkedList(ll);
    cout << *itr2 << endl;

    itr2 = ll.insert(itr2, 999);
    PrintLinkedList(ll);
    cout << *itr2 << endl;

}