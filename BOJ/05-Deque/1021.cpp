#include <iostream>
#include <deque>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, M;
    cin >> N >> M;

    queue<int> q;
    for(int i=0; i < M; i++) {
        int target;
        cin >> target;
        q.push(target);
    }

    deque<int> dq;
    for(int i=1; i <= N; i++) {
        dq.push_back(i);
    }

    int total_opts = 0;
    while(!q.empty()) {
        int target = q.front();
        q.pop();

        if(dq.front() != target) {
            // 2번 연산 횟수 계산
            int num_opt_two = 0;
            deque<int> dq_copy1(dq);
            while(dq_copy1.front() != target) {
                int value = dq_copy1.front();
                dq_copy1.pop_front();
                dq_copy1.push_back(value);
                num_opt_two++;
            }

            // 3번 연산 횟수 계산
            int num_opt_three = 0;
            deque<int> dq_copy2(dq);
            while(dq_copy2.front() != target) {
                int value = dq_copy2.back();
                dq_copy2.pop_back();
                dq_copy2.push_front(value);
                num_opt_three++;
            }

            // 더 적은 횟수의 이동 선택
            if(num_opt_two <= num_opt_three) {
                total_opts += num_opt_two;
                while(dq.front() != target) {
                    int value = dq.front();
                    dq.pop_front();
                    dq.push_back(value);
                }
            } else {
                total_opts += num_opt_three;
                while(dq.front() != target) {
                    int value = dq.back();
                    dq.pop_back();
                    dq.push_front(value);
                }
            }
        }
        dq.pop_front(); // 타겟 제거
    }

    cout << total_opts;
    return 0;
}