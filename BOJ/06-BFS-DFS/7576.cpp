#include <iostream>
#include <queue>
#include <vector>

#define X first
#define Y second

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, M;
    cin >> M >> N;

    vector<vector <int>> board(N, vector<int>(M, 0));
    vector<vector <int>> dist(N, vector<int>(M, -2));
    queue<pair <int, int>> q;
    bool all_rotten = 1;
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < M; j++)
        {
            cin >> board[i][j];
            if (board[i][j] == 0)
            {
                all_rotten = 0;
                dist[i][j] = -1;
            }

            else if(board[i][j] == 1)
            {
                q.push({i, j});
                dist[i][j] = 0;
            }
        }
    }

    if (all_rotten)
    {
        cout << 0;
        exit(0);
    }

    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};
    while(!(q.empty()))
    {
        pair<int, int> curr_coords = q.front();
        q.pop();
        int curr_dist = dist[curr_coords.X][curr_coords.Y];

        for(int i = 0; i < 4; i++)
        {
            int nx = curr_coords.X + dx[i];
            int ny = curr_coords.Y + dy[i];

            if (nx < 0 || nx >= N || ny < 0 || ny >= M)
                continue;

            if (board[nx][ny] == -1 || dist[nx][ny] != -1)
                continue;

            q.push({nx, ny});
            dist[nx][ny] = curr_dist + 1;
        }
    }

    int max_date = 0;
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < M; j++)
        {
            if(dist[i][j] == -1)
            {
                cout << -1;
                exit(0);
            }
            else if(dist[i][j] > 0)
            {
                if(dist[i][j] > max_date)
                {
                    max_date = dist[i][j];
                }
            }
        }
    }

    cout << max_date;
}