#include <iostream>
#include <stack>

using namespace std;

int main()
{
    int k = 0;
    cin >> k;

    stack<int> s;
    for(int i=0; i<k; i++)
    {
        int num = 0;
        cin >> num;

        if(num == 0)
            s.pop();
        else
            s.push(num);
    }

    int total = 0;
    for(int i = s.size(); i > 0; i--)
    {
        total += s.top();
        s.pop();
    }
    cout << total;

    return 0;
}