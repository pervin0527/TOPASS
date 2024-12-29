#include <iostream>

using namespace std;

void push(int value, int stack[], int &pos)
{
    stack[pos] = value;
    pos++;
}

void pop(int &pos)
{
    pos--;
}

int top(int stack[], int &pos)
{
    return stack[pos-1];
}

int empty(int &pos)
{
    return pos == 0 ? 1 : 0;
}

int main()
{
    const int arr_size = 1000;
    int stack[arr_size];
    int pos = 0;

    push(5, stack, pos); 
    push(4, stack, pos); 
    push(3, stack, pos);

    cout << top(stack, pos) << '\n'; // 3

    pop(pos); 
    pop(pos);

    cout << top(stack, pos) << '\n'; // 5

    push(10, stack, pos); 
    push(12, stack, pos);

    cout << top(stack, pos) << '\n'; // 12

    pop(pos);
    cout << top(stack, pos) << '\n'; // 10

    return 0;
}