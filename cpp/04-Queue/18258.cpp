#include <iostream>
#include <queue>
#include <string>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N = 0;
    cin >> N;

    queue<int> Q;
    for(int i = 0; i < N; i++)
    {
        string command;
        cin >> command;

        if(command == "push")
        {
            int value;
            cin >> value;
            Q.push(value);
        }

        else if(command == "pop")
        {
            if(!Q.empty())
            {
                cout << Q.front() << "\n";
                Q.pop();
            }
            else
            {
                cout << -1 << "\n";
            }
        }

        else if(command == "size")
        {
            cout << Q.size() << "\n";
        }

        else if(command == "empty")
        {
            if(Q.empty())
                cout << 1 << "\n";
            else
                cout << 0 << "\n";
        }

        else if(command == "front")
        {
            if(!Q.empty())
                cout << Q.front() << "\n";
            else
                cout << -1 << "\n";
        }

        else
        {
            if(!Q.empty())
                cout << Q.back() << "\n";
            else
                cout << -1 << "\n";
        }
    }
    return 0;
}