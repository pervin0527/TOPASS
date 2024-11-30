# iterator

'''
list<자료형>::iterator
'''

- 연결리스트의 반복자(iterator).
- ```std::list```는 양방향 연결 리스트로 반복자를 사용해 앞뒤로 요소 이동이 가능함.
- 반복자는 포인터처럼 ```*``` 연산자를 사용하여 값을 참조하거나, ```++```, ```--``` 연산자를 사용하여 다음 또는 이전 요소로 이동할 수 있다.

list<char> 타입의 포인터를 직접 만드는 것은 가능합니다. 하지만 그것이 연결 리스트 내부의 특정 노드를 가리키는 포인터처럼 작동하지는 않는다.  
또한 ```std::list```는 추상화된 STL 컨테이너이며, 내부 구현 세부 사항(노드 구조 등)에 직접 접근할 수 없다.

```
#include <list>
#include <iostream>

using namespace std;

int main() {
    // list<char> 객체 생성
    list<char> myList = {'a', 'b', 'c', 'd'};

    // list<char> 객체의 포인터 생성
    list<char>* myListPtr = &myList;

    // 포인터를 통해 list<char> 전체에 접근
    for (char c : *myListPtr) {
        cout << c << " ";
    }
    cout << endl;

    return 0;
}
```

```std::list<char>``` 자체는 객체이므로, 그 객체의 포인터를 생성할 수 있다. 하지만 이는 단순히 std::list<char> 전체를 가리키는 포인터일 뿐, 내부 노드를 가리키는 것이 아니다.

```
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

```