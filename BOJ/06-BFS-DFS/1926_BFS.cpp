#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define X first
#define Y second

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int rows = 0;
    int cols = 0;
    cin >> rows;
    cin >> cols;

    vector<vector<int>> board(rows, vector<int>(cols, 0));
    vector<vector<bool>> vis(rows, vector<bool>(cols, 0));

    for(int i=0; i < rows; i++)
    {
        for(int j=0; j < cols; j++)
        {
            cin >> board[i][j];
        }
    }

    queue<pair<int, int> > q;
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};

    int max_area = 0;
    int num_pics = 0;
    for(int i=0; i<rows; i++)
    {
        for(int j=0; j<cols; j++)
        {
            if(board[i][j] == 1 && vis[i][j] ==0)
            {
                q.push({i, j});
                vis[i][j] = 1;
                num_pics += 1;
            }

            int cur_area = 0;
            while(!(q.empty()))
            {
                pair<int, int> cur = q.front();
                cur_area += 1;
                q.pop();

                for(int k=0; k<4; k++)
                {
                    int nx = cur.X + dx[k];
                    int ny = cur.Y + dy[k];

                    if(nx < 0 || nx >= rows || ny < 0 || ny >= cols)
                        continue;

                    if(vis[nx][ny] == 1 || board[nx][ny] == 0)
                        continue;

                    q.push({nx, ny});
                    vis[nx][ny] = 1;
                }
            }

            if(cur_area > max_area)
                max_area = cur_area;
        }
    }

    cout << num_pics << '\n' << max_area;
}