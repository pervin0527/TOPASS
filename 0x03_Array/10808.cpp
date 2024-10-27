#include <iostream>

using namespace std;

int main()
{
    char word[101]; // 단어의 길이는 100을 넘지 않으며 모두 소문자.
    cin >> word;

    int counts[26] = {0};
    for (int i=0; word[i] != '\0'; i++)
    {
        // 아스키코드에서 'a'는 97, 'z'는 122 이므로 이를 counts의 인덱스로 사용한다.
        int idx = int(word[i]) - 97;
        counts[idx] += 1;
    }

    for (int i=0; i < 26; i++)
    {
        cout << counts[i] << " ";
    }

    return 0;
}