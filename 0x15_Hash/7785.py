import sys
input = sys.stdin.readline

def main():
    n = int(input().strip())

    answer = {}
    for _ in range(n):
        name, state = input().strip().split()
        
        # 'enter' 상태일 때 이름 추가
        if state == 'enter':
            answer[name] = state
        
        # 'leave' 상태일 때 이름 제거
        elif state == 'leave' and name in answer:
            del answer[name]

    # 남아있는 이름들을 정렬하여 출력
    remaining_names = sorted(answer.keys(), reverse=True)
    for name in remaining_names:
        print(name)

if __name__ == '__main__':
    main()