import sys
from collections import deque

def solution():
    N = int(sys.stdin.readline().rstrip())
    cards = deque([x for x in range(1, N+1)])

    while len(cards) > 1:
        _ = cards.popleft() ## 맨 위에 있는 카드 버리기.
        cards.append(cards.popleft()) ## 그 다음 맨 위에 있던 카드를 맨 밑으로 보낸다.

    print(cards[0])
        
if __name__ == "__main__":
    solution()