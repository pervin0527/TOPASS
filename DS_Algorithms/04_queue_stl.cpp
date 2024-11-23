#include <iostream>
#include <queue>

using namespace std;

int main()
{
    queue<int> q;
    q.push(10);
    q.push(20);
    q.push(30);

    cout << q.size() << "\n";

    if(q.empty())
    {
        cout << "Q is Empty\n";
    }
    else
    {
        cout << "Q is Not Empty\n";
    }

    q.pop();
    cout << q.front() << "\n";
    cout << q.back() << "\n";

    return 0;
}