#include <iostream>

using namespace std;

// 이중 연결 리스트의 노드 구조체 정의
struct Node
{
    int data;
    Node* prev;
    Node* next;

    Node(int value) : data(value), prev(nullptr), next(nullptr) {}
};

class DoublyLinkedList
{
private:
    Node* head;
    Node* tail;

public:
    DoublyLinkedList() : head(nullptr), tail(nullptr) {}

    // 리스트의 모든 노드 출력
    void traverse()
    {
        Node* current = head;
        while (current != nullptr)
        {
            cout << current->data << " ";
            current = current->next;
        }
        cout << endl;
    }

    // 특정 위치에 노드 삽입
    void insert(int idx, int value)
    {
        Node* new_node = new Node(value);

        if (idx == 0) // 리스트의 맨 앞에 삽입
        {
            if (head == nullptr) // 리스트가 비어 있는 경우
            {
                head = tail = new_node;
            }
            else
            {
                new_node->next = head;
                head->prev = new_node;
                head = new_node;
            }
            return;
        }

        // 중간 또는 끝에 삽입
        Node* current = head;
        for (int i = 0; current != nullptr && i < idx - 1; i++)
        {
            current = current->next;
        }

        if (current == nullptr) // 인덱스가 범위를 초과하는 경우
        {
            cout << "잘못된 인덱스입니다." << endl;
            delete new_node;
            return;
        }

        new_node->next = current->next;
        new_node->prev = current;

        if (current->next != nullptr) // 중간에 삽입하는 경우
        {
            current->next->prev = new_node;
        }
        else // 리스트의 끝에 삽입하는 경우
        {
            tail = new_node;
        }

        current->next = new_node;
    }

    // 특정 위치의 노드 삭제
    void erase(int idx)
    {
        if (head == nullptr) // 리스트가 비어 있는 경우
        {
            cout << "삭제할 노드가 없습니다." << endl;
            return;
        }

        Node* to_delete;

        if (idx == 0) // 리스트의 맨 앞 노드 삭제
        {
            to_delete = head;
            head = head->next;

            if (head != nullptr) // 리스트에 다른 노드가 있는 경우
            {
                head->prev = nullptr;
            }
            else // 삭제 후 리스트가 비어 있는 경우
            {
                tail = nullptr;
            }
        }
        else
        {
            Node* current = head;
            for (int i = 0; current != nullptr && i < idx - 1; i++)
            {
                current = current->next;
            }

            if (current == nullptr || current->next == nullptr) // 유효하지 않은 인덱스
            {
                cout << "잘못된 인덱스입니다." << endl;
                return;
            }

            to_delete = current->next;
            current->next = to_delete->next;

            if (to_delete->next != nullptr) // 중간 노드 삭제
            {
                to_delete->next->prev = current;
            }
            else // 리스트의 끝 노드 삭제
            {
                tail = current;
            }
        }

        delete to_delete; // 메모리 해제
    }
};

int main()
{
    DoublyLinkedList dll;
    dll.insert(0, 10);
    dll.insert(1, 20);
    dll.insert(2, 30);

    cout << "List after inserts: ";
    dll.traverse();

    dll.erase(0);
    cout << "List after deleting first node: ";
    dll.traverse();

    dll.erase(1);
    cout << "List after deleting last node: ";
    dll.traverse();

    return 0;
}
