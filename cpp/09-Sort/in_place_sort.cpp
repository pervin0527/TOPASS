#include <iostream>

using namespace std;

int arr[8] = {6, -8, 1, 12, 8, 3, 7, -7};

int main()
{
    int pivot = arr[0];
    int *ptr_a = arr+1;
    int *ptr_b = arr+7;

    for(const auto e : arr)
        cout << e << " ";
    cout << "\n";

    // cout << ptr_a << " " << ptr_b << endl; // 주소값
    // cout << *ptr_a << " " << *ptr_b << endl; // 주소에 저장된 실제값
    
    // 포인터 l이 포인터 r보다 왼쪽에 있을 경우에만 in-place sort를 수행.
    while(ptr_a < ptr_b)
    {
        // l포인터가 가리키는 원소가 피벗보다 작은값이며 r포인터보다 왼쪽에 있는 경우.
        // l이 계속 오른쪽으로 이동하다보니 ptr_a < ptr_b를 지속적으로 확인해야함.
        while(*ptr_a < pivot && ptr_a < ptr_b)
            ptr_a++;

        while(*ptr_b > pivot && ptr_a < ptr_b)
            ptr_b--;

        if(ptr_a < ptr_b)
        {
            swap(*ptr_a, *ptr_b);
        }

    }

    swap(arr[0], *ptr_b);

    for(const auto e : arr)
        cout << e << " ";
    cout << "\n";

    return 0;
}