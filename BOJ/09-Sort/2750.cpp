#include <iostream>
#include <vector>

using namespace std;

void merge(int st, int en, vector<int> &arr, vector<int> &tmp)
{
    int mid = (st + en) / 2;
    int lidx = st;
    int ridx = mid;

    for(int i = st; i < en; i++)
    {
        if(ridx == en)
            tmp[i] = arr[lidx++];
        else if(lidx == mid)
            tmp[i] = arr[ridx++];
        else if(arr[lidx] <= arr[ridx])
            tmp[i] = arr[lidx++];
        else
            tmp[i] = arr[ridx++];
    }

    for(int i = st; i < en; i++)
        arr[i] = tmp[i];
}

void merge_sort(int st, int en, vector<int> &arr, vector<int> &tmp)
{
    if(st + 1 == en)
        return;

    int mid = (st + en) / 2;
    merge_sort(st, mid, arr, tmp);
    merge_sort(mid, en, arr, tmp);
    merge(st, en, arr, tmp);
}

int main()
{
  ios::sync_with_stdio(0);
  cin.tie(0);

    // Input
    int n;
    cin >> n;

    vector<int> arr(n, 0);
    vector<int> tmp(n, 0);
    for(int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    // Sorting
    merge_sort(0, n, arr, tmp);
    for(int i = 0; i < n; i++)
        cout << arr[i] << "\n";
}