#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n;
  cin >> n;
  
  stack<int> S;
  
  int cnt = 1;
  string ans;

  while (n--) {
    // 수열에서 현재 보고 있는 수(타겟)
    int t;
    cin >> t;

    // t가 스택의 top에 올 때까지 오름차순으로 push()
    while (cnt <= t) {
      S.push(cnt++); // 1 -> 2 -> 3 -> ... -> t
      ans += "+\n";
    }

    // 스택의 top과 t가 같지 않은 경우 수열을 만들 수 없음.
    if (S.top() != t) { 
      cout << "NO\n";
      return 0;
    }

    // 스택의 top과 t가 같으니까 pop()
    S.pop();
    ans += "-\n";
  }
  cout << ans;
}