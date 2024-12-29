#include <iostream>
#include <stack>
#include <vector>

#define X first
#define Y second

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, M;
    cin >> N >> M;

    vector<vector <int>> board(N, vector<int>(M, 0));
    vector<vector <bool>> vis(N, vector<bool>(M, 0));

    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < M; j++)
        {
            cin >> board[i][j];
        }
    }

    stack<pair <int, int>> s;
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};

    int num_pics = 0;
    int max_area = 0;

    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < M; j++)
        {
            if(board[i][j] == 1 && vis[i][j] == 0)
            {
                s.push({i, j});
                vis[i][j] = 1;
                num_pics++;
            }

            int curr_area = 0;
            while(!(s.empty()))
            {
                pair<int, int> curr = s.top();
                s.pop();
                curr_area++;

                for(int k = 0; k < 4; k++)
                {
                    int nx = curr.X + dx[k];
                    int ny = curr.Y + dy[k];

                    if(nx < 0 || nx >= N || ny < 0 || ny >= M)
                        continue;

                    if(board[nx][ny] == 0 || vis[nx][ny] == 1)
                        continue;

                    s.push({nx, ny});
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