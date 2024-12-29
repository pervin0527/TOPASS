#include <iostream>

using namespace std;

int n = 10;
int arr[1000001] = {15, 25, 22, 357, 16, 23, -53, 12, 46, 3};
int tmp[1000001];

void merge(int st, int en)
{
    int mid = (st + en) / 2;
    int lidx = st;
    int ridx = mid;

    for(int i = st; i < en; i++)
    {
        // 오른쪽 배열에서 탐색할 원소가 남아있지 않을 때
        if(ridx == en)
            tmp[i] = arr[lidx++];

        // 왼쪽 배열에서 탐색할 원소가 남아있지 않을 때
        else if(lidx == mid)
            tmp[i] = arr[ridx++];

        // 왼쪽 배열의 lidx번째 원소가 오른쪽 배열의 ridx번째 원소보다 작거나 같을 때(stable sort)
        else if(arr[lidx] <= arr[ridx])
            tmp[i] = arr[lidx++];

        // 오른쪽 배열의 ridx번째 원소가 왼쪽 배열의 lidx번째 원소보다 작을 때
        else
            tmp[i] = arr[ridx++];
    }

    // tmp 배열의 값을 arr 배열로 복사.
    for(int i = st; i < en; i++)
        arr[i] = tmp[i];
}

void merge_sort(int st, int en)
{
    if(en == st + 1) // 배열의 길이가 1일 때를 의미함.
        return;

    int mid = (st + en) / 2;
    merge_sort(st, mid);
    merge_sort(mid, en);
    merge(st, en);
}

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    merge_sort(0, n);
    for(int i = 0; i < n; i++)
        cout << arr[i] << " ";
}