#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    stack<int> s;

    int commands = 0;
    cin >> commands;

    for(int i=0; i<commands; i++)
    {
        string command;
        cin >> command;

        if(command == "push")
        {
            int value = 0;
            cin >> value;
            s.push(value);
        }

        else if(command == "pop")
        {
            if(s.empty())
                cout << -1 << '\n';
            else
            {
                cout << s.top() << '\n';
                s.pop();
            }
        }

        else if(command == "size")
        {
            cout << s.size() << '\n';
        }

        else if(command == "empty")
        {
            if(s.empty())
                cout << 1 << '\n';
            else
                cout << 0 << '\n';
        }

        else
        {
            if(s.empty())
                cout << -1 << '\n';
            else
                cout << s.top() << '\n';
        }

    }
}