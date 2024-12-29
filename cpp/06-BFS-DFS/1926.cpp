#include <iostream>
#include <queue>
#include <vector>

#define X first
#define Y second

using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;

    vector<vector <bool>> vis(N, vector<bool>(M, 0));
    vector<vector <int>> board(N, vector<int> (M, 0));
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < M; j++)
        {
            cin >> board[i][j];
        }
    }

    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};
    queue<pair <int, int>> q;

    int num_pics = 0;
    int max_area = 0;
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < M; j++)
        {
            if(board[i][j] == 1 && vis[i][j] == 0)
            {
                q.push({i, j});
                vis[i][j] = 1;
                num_pics += 1;
            }

            int curr_area = 0;
            while(!(q.empty()))
            {
                pair <int, int> curr = q.front();
                q.pop();
                curr_area += 1;

                for(int k = 0; k < 4; k++)
                {
                    int nx = curr.X + dx[k];
                    int ny = curr.Y + dy[k];

                    if(nx < 0 || nx >= N || ny < 0 || ny >= M)
                        continue;
                    
                    if(board[nx][ny] == 0 || vis[nx][ny] == 1)
                        continue;

                    q.push({nx, ny});
                    vis[nx][ny] = 1;
                }
            }

            if(curr_area > max_area)
                max_area = curr_area;
        }
    }

    cout << num_pics << "\n" << max_area;

    return 0;
}