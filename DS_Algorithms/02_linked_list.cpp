#include <iostream>

using namespace std;

struct Node
{
    int data;
    Node *next;

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
    Node *head;

public:
    LinkedList()
    {
        num_nodes = 0;
        head = nullptr;
    }

    void traverse()
    {
        Node *curr_node = head;
        while (curr_node != nullptr)
        {
            cout << curr_node->data << " ";
            curr_node = curr_node->next;
        }
        cout << "\n\n";
    }

    void insert(int idx, int value)
    {
        if (idx < 0 || idx > num_nodes)
        {
            cout << "Wrong Index" << endl;
            return;
        }

        Node *new_node = new Node(value);
        if (idx == 0)
        {
            new_node->next = head;
            head = new_node;
            num_nodes++;
            return;
        }

        Node *curr_node = head;
        for (int i = 0; i < idx - 1; i++)
        {
            curr_node = curr_node->next;
        }

        new_node->next = curr_node->next;
        curr_node->next = new_node;
        num_nodes++;
    }

    void erase(int idx)
    {
        if (idx < 0 || idx >= num_nodes)
        {
            cout << "Wrong Index" << endl;
            return;
        }

        if (idx == 0)
        {
            Node *target_node = head;
            head = target_node->next;
            delete target_node;
            num_nodes--;
            return;
        }

        Node *curr_node = head;
        for (int i = 0; i < idx - 1; i++)
        {
            curr_node = curr_node->next;
        }

        Node *target_node = curr_node->next;
        curr_node->next = target_node->next;
        delete target_node;
        num_nodes--;
    }
};

int main()
{
    LinkedList ll;
    ll.insert(0, 10);
    ll.insert(1, 20);
    ll.insert(2, 30);
    ll.traverse();

    ll.insert(0, 7);
    ll.traverse();

    ll.insert(2, 17);
    ll.traverse();

    ll.insert(4, 40);
    ll.traverse();

    ll.erase(0);
    ll.traverse();

    ll.erase(3);
    ll.traverse();

    ll.erase(1);
    ll.traverse();

    return 0;
}
