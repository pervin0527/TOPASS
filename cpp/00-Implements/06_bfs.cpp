#include <iostream>

using namespace std;

// first를 X, second를 Y로 설정.
#define X first
#define Y second

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int board[502][502] = {0};
    bool visited[502][502];
    int rows = 7;
    int cols = 10;

    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, 1, 0, -1};

    queue<pair<int, int> > q;
    visited[0][0] = 1;
    q.push({0, 0});

    while(!q.empty())
    {
        pair<int, int> cur = q.front();
        q.pop();
        cout << '(' << cur.X << ", " << cur.Y << ") ->";

        for(int dir=0; dir<4; dir++)
        {
            int nx = cur.X + dx[dir];
            int ny = cur.Y + dy[dir];

            if(nx < 0 || nx >= rows || ny < 0 || ny >= cols)
                continue;
            if(visited[nx][ny] || board[nx][ny] != 1)
                continue;

            visited[nx][ny] = 1;
            q.push({nx, ny});
        }
    }

}

