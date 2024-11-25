#include <iostream>
#include <string>
#include <deque>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;

    deque<int> DQ;
    for(int i=N; i > 0; i--)
    {
        string command;
        cin >> command;

        if(command == "push_front")
        {
            int value;
            cin >> value;
            DQ.push_front(value);
        }

        else if(command == "push_back")
        {
            int value;
            cin >> value;
            DQ.push_back(value);
        }

        else if(command == "pop_front")
        {
            if(DQ.empty())
                cout << -1 << "\n";
            else
            {
                cout << DQ.front() << "\n";
                DQ.pop_front();
            }
        }

        else if(command == "pop_back")
        {
            if(DQ.empty())
                cout << -1 << "\n";
            else
            {
                cout << DQ.back() << "\n";
                DQ.pop_back();
            }
        }

        else if(command == "size")
        {
            cout << DQ.size() << "\n";
        }

        else if(command == "empty")
        {
            if(DQ.empty())
                cout << 1 << "\n";
            else
                cout << 0 << "\n";
        }

        else if(command == "front")
        {
            if(DQ.empty())
                cout << -1 << "\n";
            else
                cout << DQ.front() << "\n";
        }

        else if(command == "back")
        {
            if(DQ.empty())
                cout << -1 << "\n";
            else
                cout << DQ.back() << "\n";
        }
    }


    return 0;
}