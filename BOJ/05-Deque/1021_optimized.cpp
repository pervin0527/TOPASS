#include <iostream>
#include <deque>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, M;
    cin >> N >> M;

    vector<int> targets(M);
    for(int i = 0; i < M; i++) {
        cin >> targets[i];
        targets[i]--; // 0-based 인덱스로 변환 (1, 2, 3 ---> 0, 1, 2)
    }

    deque<int> dq;
    for(int i = 0; i < N; i++) {
        dq.push_back(i); // 0-based 인덱스 사용 (1, 2, 3, 4, 5 ---> 0, 1, 2, 3, 4)
    }

    int total_opts = 0;
    for(int i = 0; i < M; i++) {
        int target = targets[i];
        
        // 현재 타겟의 위치 찾기
        int idx = 0;
        for(int j = 0; j < dq.size(); j++) {
            if(dq[j] == target) {
                idx = j;
                break;
            }
        }

        // 왼쪽, 오른쪽 중 더 가까운 방향 선택
        int left_moves = idx;
        int right_moves = dq.size() - idx;
        
        if(left_moves <= right_moves) {
            total_opts += left_moves;
            for(int j = 0; j < left_moves; j++) {
                dq.push_back(dq.front());
                dq.pop_front();
            }
        } else {
            total_opts += right_moves;
            for(int j = 0; j < right_moves; j++) {
                dq.push_front(dq.back());
                dq.pop_back();
            }
        }
        
        dq.pop_front(); // 타겟 제거
    }

    cout << total_opts;
    return 0;
}