#include <iostream>
#include <queue>
#include <vector>
#include <string>

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
    vector<vector <int>> dist(N, vector<int>(M, -1));

    for(int i = 0; i < N; i++)
    {
        string line;
        cin >> line;
        for(int j = 0; j < M; j++)
        {
            board[i][j] = line[j] - '0'; // line[j]는 문자 1이기 때문에 int로 변환하면 49가 나오기 때문에 48인 '0'을 빼준다.
        }
    }

    queue<pair<int, int>> q;
    q.push({0, 0});
    dist[0][0] = 1;

    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};
    while(!(q.empty()))
    {
        pair<int, int> curr_coords = q.front();
        q.pop();

        int curr_dist = dist[curr_coords.X][curr_coords.Y];

        for(int k = 0; k < 4; k++)
        {
            int nx = curr_coords.X + dx[k];
            int ny = curr_coords.Y + dy[k];

            if(nx < 0 || nx >= N || ny < 0 || ny >= M)
                continue;

            if(board[nx][ny] == 0 || dist[nx][ny] != -1)
                continue;

            q.push({nx, ny});
            dist[nx][ny] = curr_dist + 1;
        }
    }
    cout << dist[N-1][M-1];
}