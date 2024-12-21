#include <iostream>

using namespace std;

int n = 0;
int arr[1001];
int tmp[1001];

void quick_sort(int st, int en)
{
    // 현재 단계에서 배열의 길이가 1 이하인 경우 종료.
    if(en <= st+1)
        return;

    int pivot = arr[st]; // 각 단계별 배열의 첫번째 원소가 피벗
    int l = st + 1;
    int r = en - 1;

    while(true)
    {
        // l과 r이 서로 교차하지 않으면서 arr[l]이 pivot보다 작은 경우 l을 오른쪽으로 이동.
        // 즉, pivot보다 l이 가리키는 원소가 더 큰 경우 피벗의 오른쪽에 있어야하므로 이를 골라내기 위함.
        while(l <= r && arr[l] <= pivot)
            l++;
        
        while(l <= r && arr[r] >= pivot)
            r--;


        if (l > r)
            break;

        // 현재 l과 r이 가리키는 원소를 서로 swap.
        // 이를 통해 제자리를 찾은 Pivot의 오른쪽에는 pivot보다 큰 원소들, 왼쪽에는 Pivot보다 작은 원소들이 위치하게 된다.
        swap(arr[l], arr[r]);
    }
    // r이 가리키는 원소와 pivot의 위치를 swap.(pivot이 제자리를 찾아 가는 것.)
    swap(arr[st], arr[r]); 
    quick_sort(st, r);
    quick_sort(r+1, en);
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for(int i = 0; i < n; i++)
        cin >> arr[i];

    quick_sort(0, n);
    for(int i = 0; i < n; i++)
        cout << arr[i] << "\n";
}