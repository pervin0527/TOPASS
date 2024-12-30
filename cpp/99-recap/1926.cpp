#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int num_pics = 0;
    int max_size = 0;

    int rows, cols;
    cin >> rows >> cols;

    vector<vector<int>> vist(rows, vector<int>(cols, 0));
    vector<vector<int>> board(rows, vector<int>(cols, 0));
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            cin >> board[i][j];
        }
    }

    queue<pair<int, int>> q;
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            if (board[i][j] == 1 && vist[i][j] == 0)
            {
                q.push({i, j});
                vist[i][j] = 1;
                num_pics++;
            }

            int curr_size = 0;
            while (!q.empty())
            {
                pair<int, int> curr = q.front();
                q.pop();
                curr_size++;

                for (int k = 0; k < 4; k++)
                {
                    int nx = curr.first + dx[k];
                    int ny = curr.second + dy[k];

                    if (nx < 0 || nx >= rows || ny < 0 || ny >= cols)
                        continue;

                    if (board[nx][ny] == 0 || vist[nx][ny] == 1)
                        continue;

                    q.push({nx, ny});
                    vist[nx][ny] = 1;
                }
            }

            if (curr_size > max_size)
                max_size = curr_size;
        }
    }

    cout << num_pics << "\n"
         << max_size;
}