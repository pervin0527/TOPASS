#include <iostream>

using namespace std;

const int MAX = 1000005;
int dq[2 * MAX + 1];
int head = MAX, tail = MAX;

void push_front(int x)
{
    head -= 1;
    dq[head] = x;
}

void push_back(int x)
{
    dq[tail] = x;
    tail += 1;
}

void pop_front()
{
    head += 1;
}

void pop_back()
{
    tail -= 1;
}

int front()
{
    return dq[head];
}

int back()
{
    return dq[tail-1];
}


void test(){
  push_back(30); // 30
  cout << head << " " << tail << " " << front() << '\n'; // 30
  cout << head << " " << tail << " " << back() << '\n'; // 30

  push_front(25); // 25 30
  cout << head << " " << tail << " " << front() << '\n'; // 25
  cout << head << " " << tail << " " << back() << '\n'; // 30
  
  push_back(12); // 25 30 12
  cout << head << " " << tail << " " << front() << '\n'; // 25
  cout << head << " " << tail << " " << back() << '\n'; // 12

  push_back(62); // 25 30 12 62
  pop_front(); // 30 12 62
  cout << front() << '\n'; // 30

  pop_front(); // 12 62
  cout << back() << '\n'; // 62
}



int main()
{
    cout << head << " " << tail << "\n";
    test();
}