#include <iostream>

using namespace std;

void push(int value, int queue[], int &tail, int head, const int arr_len)
{
    // 큐가 꽉 찬 상태인지 확인
    if ((tail + 1) % arr_len == head) {
        cout << "Queue is full\n";
        return;
    }
    queue[tail] = value;
    tail = (tail + 1) % arr_len;
}

void pop(int queue[], int &head, int tail, const int arr_len)
{
    // 큐가 비어있는 상태인지 확인
    if (head == tail) {
        cout << "Queue is empty\n";
        return;
    }
    head = (head + 1) % arr_len;
}

void rear(int queue[], int tail, const int arr_len)
{
    if (tail == 0) {
        cout << "Rear: " << queue[arr_len - 1] << "\n";
    } else {
        cout << "Rear: " << queue[(tail - 1 + arr_len) % arr_len] << "\n";
    }
}

void front(int queue[], int head)
{
    cout << "Front: " << queue[head] << "\n";
}

int main()
{
    const int arr_len = 8;
    int queue[arr_len];
    int head = 0;
    int tail = 0;

    // 테스트 케이스
    push(10, queue, tail, head, arr_len);
    push(20, queue, tail, head, arr_len);
    push(30, queue, tail, head, arr_len);
    push(40, queue, tail, head, arr_len);
    front(queue, head);
    rear(queue, tail, arr_len);

    pop(queue, head, tail, arr_len);
    front(queue, head);

    push(50, queue, tail, head, arr_len);
    rear(queue, tail, arr_len);

    return 0;
}