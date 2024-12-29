#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main()
{
    // 입출력 최적화
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N = 0;
    cin >> N;

    stack<int> s;
    for(int i = 0; i < N; i++)
    {
        string command;
        cin >> command;

        if(command == "push")
        {
            int input_value = 0;
            cin >> input_value;
            s.push(input_value);
        }
        else if(command == "pop")
        {
            if (s.empty())
                cout << -1 << '\n';
            else {
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
            cout << (s.empty() ? 1 : 0) << '\n';
        }
        else // top
        {
            cout << (s.empty() ? -1 : s.top()) << '\n';
        }
    }

    return 0;
}