#include <iostream>
#include <list>

using namespace std;

int main()
{
    list<int> ll;

    ll.push_back(22);
    ll.push_back(33);
    ll.push_front(11);
    ll.push_back(44);
    ll.push_back(55);
    // [22, 33, 11, 44, 55]

    for (const auto node : ll)
        cout << node << " ";
    cout << "\n";

    /*
    연결리스트의 마지막을 가리키는 iterator.
    마지막 노드를 가리키는 것이 아니라, 연결 리스트의 범위를 벗어난 다음 위치를 가리키는 이터레이터를 반환한다.
    */
    list<int>::iterator itr_end = ll.end();
    cout << "연결리스트의 마지막 원소 : " << *itr_end << "\n\n"; // 포인터 연산자를 사용해서 현재 iterator가 가리키고 있는 원소가 무엇인지 확인할 수 있다.

    // itr을 뒤로(왼쪽 방향)으로 한 칸 이동 시키면 마지막 노드를 가리키고 있음.
    itr_end--;
    cout << "연결리스트의 마지막 원소 : " << *itr_end << "\n\n";

    // iterator와 next, begin을 활용.
    // begin은 ll의 첫번째 노드를 가리키는 iterator이고 next는 두번째 인자만큼 itr을 오른쪼으로 이동시키는 역할을 함.
    ll.insert(next(ll.begin(), 1), 17); // 1번 idx에 17을 삽입.
    cout << "연결리스트의 1번 인덱스에 17 삽입." << "\n";
    for (const auto node : ll)
        cout << node << " ";
    cout << "\n\n";

    // iterator만 활용.
    list<int>::iterator itr_begin = ll.begin();
    cout << "연결리스트의 2번 인덱스에 27 삽입" << "\n";
    for (int i = 0; i < 2; i++)
        // 0번 인덱스 → 1번 인덱스 이동
        // 1번 인덱스 → 2번 인덱스 이동
        itr_begin++;
    ll.insert(itr_begin, 27);

    for (const auto node : ll)
        cout << node << " ";
    cout << "\n\n";
}