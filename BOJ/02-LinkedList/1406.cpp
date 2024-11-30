#include <list>
#include <string>
#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    string line;
    cin >> line;
    cin >> n;

    list<char> ll;
    for (int i = 0; i < line.size(); i++)
    {
        ll.push_back(line[i]);
    }
    
    // 커서를 문자열의 끝으로 초기화
    list<char>::iterator cursor = ll.end(); // iterator는 list 클래스의 멤버
    for (int i = 0; i < n; i++)
    {
        char command;
        cin >> command;

        if (command == 'L')
        {
            // 커서가 맨 왼쪽이 아니라면 왼쪽으로 이동
            if (cursor != ll.begin())
                --cursor;
        }
        else if (command == 'D')
        {
            // 커서가 맨 끝이 아니라면 오른쪽으로 이동
            if (cursor != ll.end())
                ++cursor;
        }
        else if (command == 'B')
        {
            // 커서가 맨 왼쪽이 아니라면 현재 문자를 삭제
            if (cursor != ll.begin())
            {
                cursor = ll.erase(--cursor);
            }
        }
        else if (command == 'P')
        {
            // 새로운 문자를 입력받아 커서 왼쪽에 추가
            char value;
            cin >> value;
            ll.insert(cursor, value);
        }
    }

    // 리스트의 모든 문자를 출력
    for (char c : ll)
    {
        cout << c;
    }

    return 0;
}
