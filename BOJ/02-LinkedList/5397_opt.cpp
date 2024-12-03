#include <iostream>
#include <list>
#include <string>

using namespace std;

string getPassword(const string& input) {
    list<char> password;
    auto cursor = password.begin();

    for (char c : input) {
        if (c == '<') {
            if (cursor != password.begin()) {
                cursor--;
            }
        }
        else if (c == '>') {
            if (cursor != password.end()) {
                cursor++;
            }
        }
        else if (c == '-') {
            if (cursor != password.begin()) {
                cursor = password.erase(--cursor);
            }
        }
        else {
            password.insert(cursor, c);
        }
    }

    string result;
    for (char c : password) {
        result += c;
    }
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int T;
    cin >> T;
    
    while (T--) {
        string input;
        cin >> input;
        cout << getPassword(input) << '\n';
    }
    
    return 0;
}