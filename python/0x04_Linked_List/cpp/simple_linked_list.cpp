#include <iostream>

using namespace std;

struct Node
{
    int data;
    Node* next;

    // 구조체 멤버 함수(생성자)
    Node(int value)
    {
        data = value;
        next = nullptr;
    }
};

class LinkedList
{
private:
    int num_nodes;
    Node* head;

public:
    LinkedList()
    {
        num_nodes = 0;
        head = nullptr;
    }

    void traverse()
    {
        Node* curr = head;
        while (curr != nullptr)
        {
            cout << curr->data << " ";
            curr = curr->next;
        }
        cout << endl;
    }

    void insert(int idx, int value)
    {
        if (idx < 0 || idx > num_nodes)
        {
            cout << "잘못된 인덱스입니다." << endl;
            return;
        }

        Node* new_node = new Node(value); // 동적 할당으로 신규노드 생성

        // 맨 앞에 삽입하는 경우
        if (idx == 0)
        {
            new_node->next = head;
            head = new_node;
            num_nodes++;
            return;
        }

        // 중간이나 끝에 삽입하는 경우
        Node* current = head;
        for (int i = 0; i < idx - 1; i++)
        {
            current = current->next;
        }

        new_node->next = current->next;
        current->next = new_node;
        num_nodes++;
    }

    void erase(int idx)
    {
        // 인덱스가 유효하지 않은 경우
        if (idx < 0 || idx >= num_nodes)
        {
            cout << "잘못된 인덱스입니다." << endl;
            return;
        }

        Node* to_delete;

        // 맨 앞 노드 삭제
        if (idx == 0)
        {
            to_delete = head;
            head = head->next;
        }
        else
        {
            // 중간 또는 끝 노드 삭제
            Node* current = head;
            for (int i = 0; i < idx - 1; i++)
            {
                current = current->next;
            }
            
            to_delete = current->next;
            current->next = to_delete->next;
        }

        delete to_delete; // 메모리 해제
        num_nodes--; // 노드 개수 업데이트
    }

};

int main()
{
    LinkedList ll;
    ll.insert(0, 5);
    ll.insert(1, 7);
    ll.insert(2, 9);

    ll.traverse();

    ll.erase(0);
    ll.traverse();

    ll.erase(1);
    ll.traverse();

    return 0;
}