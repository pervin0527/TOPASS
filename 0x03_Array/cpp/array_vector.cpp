#include <iostream>
#include <vector>

using namespace std;

void PrintVector(vector<int> &v)
{
    for (int item : v)
    {
        cout << item << " ";
    }
    cout << "\n\n";
}

int main()
{
    vector<int> v1 = {1, 3, 5};
    v1.insert(v1.begin()+1, 2); // {1, 2, 3, 5}
    PrintVector(v1);

    v1.push_back(6); // {1, 2, 3, 5, 6}
    PrintVector(v1);

    v1.insert(v1.begin()+3, 4);
    PrintVector(v1);

    v1.pop_back();
    PrintVector(v1);

    return 0;
}