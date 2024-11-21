#include <iostream>
#include <vector>

using namespace std;

void PrintVec(vector<int> &v)
{
    for(int i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
    cout << "\n";
}

int main()
{
    vector<int> v1 = {10, 20, 30, 40, 50, 60};
    cout << v1.size() << '\n';

    v1.push_back(70);
    v1.insert(v1.begin(), 7);
    v1.insert(v1.begin()+1, 17);

    PrintVec(v1);

    v1.pop_back();
    v1.erase(v1.begin());
    v1.erase(v1.end()-2);

    PrintVec(v1);

    return 0;
}