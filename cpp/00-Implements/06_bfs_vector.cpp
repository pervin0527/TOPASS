#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define X first
#define Y second

int main()
{
    int rows, cols;
    cin >> rows >> cols;

    // 2차원 배열 정의.
    // vector<int>를 자료형으로 하는 vector를 생성한다.
    vector<vector<int>> board(rows, vector<int>(cols, 0));
    vector<vector<bool>> visited(rows, vector<bool>(cols, 0));
    for(int i=0; i<rows; i++){
        for(int j=0; j<cols; j++){
            cin >> board[i][j];
        }
    }

    queue <pair<int, int>> q;
    int dx[4] = {0, 0, -1, 1};
    int dy[4] = {-1, 1, 0, 0};

    int num_pics = 0;
    int max_area = 0;
    for(int x=0; x<rows; x++){
        for(int y=0; y<cols; y++){
            if(board[x][y] == 1 && visited[x][y] == 0)
            {
                q.push({x, y});
                num_pics += 1;
                visited[x][y] = 1;
            }

            int cur_area = 0;
            while(!(q.empty()))
            {
                pair<int, int> cur = q.front();
                q.pop();
                cur_area += 1;

                for(int i=0; i<4; i++)
                {
                    int nx = cur.X + dx[i];
                    int ny = cur.Y + dy[i];

                    if(nx < 0 || nx >= rows || ny < 0 || ny >= cols)
                        continue;

                    if(board[nx][ny] == 0 || visited[nx][ny] == 1)
                        continue;

                    q.push({nx, ny});
                    visited[nx][ny] = 1;
                }
            }

            if(cur_area > max_area)
                max_area = cur_area;
        }
    }
    cout << num_pics << "\n" << max_area;

    return 0;
}