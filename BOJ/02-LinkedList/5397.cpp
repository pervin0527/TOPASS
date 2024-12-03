#include <iostream>
#include <list>
#include <string>

using namespace std;

int main()
{
    int n;
    cin >> n;

    for(int i = 0; i < n; i++)
    {
        string line;
        cin >> line;

        list<char> ll;
        auto itr = ll.begin();
        for (char ch : line)
        {
            if (ch == '<')
            {
                if (itr != ll.begin())
                    --itr;
            }
            else if (ch == '>')
            {
                if (itr != ll.end())
                    ++itr;
            }
            else if (ch == '-')
            {
                if (!ll.empty() && itr != ll.begin()) // 빈 리스트일 경우 검사 추가
                {
                    --itr; // iterator 이동
                    itr = ll.erase(itr); // 요소 삭제
                }
            }
            else
            {
                ll.insert(itr, ch); // 문자 삽입
                cout << *itr << endl;
            }
        }

        for(const auto item : ll)
        {
            cout << item;
        }
        cout << "\n";
    }
}