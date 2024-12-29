#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    vector<int> a(n), b(m);

    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < m; i++) cin >> b[i];

    int a_idx = 0, b_idx = 0;

    // 병합하며 바로 출력
    while (a_idx < n && b_idx < m) {
        if (a[a_idx] < b[b_idx]) {
            cout << a[a_idx++] << " ";
        } else {
            cout << b[b_idx++] << " ";
        }
    }

    // 남은 요소 바로 출력
    while (a_idx < n) cout << a[a_idx++] << " ";
    while (b_idx < m) cout << b[b_idx++] << " ";

    return 0;
}
