#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n, m;
    cin >> n >> m;

    vector<int> a(n, 0);
    vector<int> b(m, 0);
    vector<int> res(n+m, 0);

    for(int i = 0; i < n; i++)
        cin >> a[i];

    for(int i = 0; i < m; i++)
        cin >> b[i];

    int a_idx = 0;
    int b_idx = 0;
    for(int i = 0; i < n+m; i++)
    {
        if(a_idx < n && b_idx < m)
        {
            if(a[a_idx] < b[b_idx])
            {
                res[i] = a[a_idx];
                a_idx++;
            }
            else
            {
                res[i] = b[b_idx];
                b_idx++;
            }
        }
        else if(a_idx >= n && b_idx < m)
        {
            res[i] = b[b_idx];
            b_idx++;
        }
        else if(a_idx < n && b_idx >= m)
        {
            res[i] = a[a_idx];
            a_idx++;
        }
    }

    for(const auto i : res)
        cout << i << " ";
}