#include <iostream>
using namespace std;

int main()
{
    int n = 7;
    int arr[7] = {7, 2, 0, 1, 5, 6, 4};

    for(int j = 0; j < n; j++)
    {
        bool swapped = false; // 교환이 발생했는지 확인하는 플래그
        for(int i = 0; i < n - 1 - j; i++) // 이미 정렬된 부분은 제외
        {
            if(arr[i] > arr[i+1])
            {
                swap(arr[i], arr[i+1]);
                swapped = true; // 교환이 발생했음을 기록
            }
        }

        // 현재 배열 상태 출력 (디버깅 용도)
        for(const auto e : arr)
        {
            cout << e << " ";
        }
        cout << "\n";

        if(!swapped) // 교환이 발생하지 않았다면 정렬 완료
        {
            break;
        }
    }
}
