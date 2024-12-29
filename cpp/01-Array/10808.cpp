#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    string word;
    getline(cin, word);
    
    // int arr[26] = {0};
    vector<int> arr(26, 0);
    for(int i=0; i<word.length(); i++)
    {
        int w = word[i] - 97; // 각각의 알파벳을 정수형 아스키코드로 변환.
        arr[w] += 1;
    }

    for(int i=0; i<26; i++)
    {
        cout << arr[i] << " ";
    }

    return 0;
}