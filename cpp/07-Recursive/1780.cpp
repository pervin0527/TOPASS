#include <iostream>
#include <vector>

using namespace std;

bool check(vector<vector<int>> &arr, int sr, int sc, int size)
{
    int first_elem = arr[sr][sc];  // 부분 행렬의 첫 번째 원소

    for(int i = sr; i < sr + size; i++)
    {
        for(int j = sc; j < sc + size; j++)
        {
            if(arr[i][j] != first_elem)
            {
                return false;
            }
        }
    }
    return true;
}

void func(vector<vector<int>> &arr, int sr, int sc, int size, int res[])
{
    if(size == 0)
        return;

    if(check(arr, sr, sc, size))
    {
        int r = arr[sr][sc];
        
        // res는 0, 1, 2로 인덱스가 구성되고 r은 -1, 0, 1이므로 값을 조정해야함.
        // -1 -> 0, 0 -> 1, 1 -> 2 
        res[r + 1] += 1;
        return;
    }

    int new_size = size / 3;
    for(int i = 0; i < 3; i++)
    {
        for(int j = 0; j < 3; j++)
        {
            // i = 0, j = 0 --> 0 + 0 * 3 = 0, 0 + 0 * 3 = 0 --> (0, 0, 3)
            // i = 0, j = 1 --> 0 + 0 * 3 = 0, 0 + 1 * 3 = 3 --> (0, 3, 3)
            func(arr, sr + i * new_size, sc + j * new_size, new_size, res);
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    int res[3] = {0, 0, 0};  // -1의 개수, 0의 개수, 1의 개수
    vector<vector<int>> mat(n, vector<int>(n, 0));
    
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            cin >> mat[i][j];
        }
    }

    func(mat, 0, 0, n, res);

    cout << res[0] << "\n";  // -1의 개수
    cout << res[1] << "\n";  // 0의 개수
    cout << res[2] << "\n";  // 1의 개수

    return 0;
}