#include <iostream>
#include <queue>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    queue<int> Q;

    for(int i=1; i < (N+1); i++)
    {
        Q.push(i);
    }

    while(Q.size() > 1)
    {
        Q.pop();

        int front_value = Q.front();
        Q.pop();
        Q.push(front_value);
    }

    cout << Q.front() << "\n";

    return 0;
}