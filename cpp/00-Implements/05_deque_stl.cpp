#include <iostream>
#include <deque>

using namespace std;

int main()
{
    deque<int> dq;
    
    dq.push_front(10);
    dq.push_back(50);
    dq.push_front(24);

    for (auto x : dq)
        cout << x << " ";

    cout << dq.size() << "\n";

    if (dq.empty())
        cout << "dq is empty\n";
    else
        cout << "dq is not empty\n";

    dq.pop_front();
    dq.pop_back();

    cout << dq.back() << "\n";
    
    dq.push_back(72);
    cout << dq.front() << "\n";

    cout << dq.front() << "\n";
}