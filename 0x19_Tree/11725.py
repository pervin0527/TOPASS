import sys
from collections import deque

def solution1():
    num_nodes = int(sys.stdin.readline().strip())

    adj_list = [[] for _ in range(num_nodes + 1)] ## 인덱스를 1부터 사용하기 위해 +1
    for _ in range(num_nodes - 1): ## 트리는 V개의 노드와 V-1개의 엣지로 구성되기 때문에 -1
        u, v = map(int, sys.stdin.readline().strip().split())

        ## 트리는 무방향 그래프이기 때문에 양방향 연결을 한다.
        adj_list[u].append(v)
        adj_list[v].append(u)

    ## BFS로 탐색하면서 현재 노드의 부모가 어떤 노드인지 기록한다.
    queue = deque()
    queue.append(1)
    parent_list = [0] * (num_nodes + 1) ## 각 노드의 부모를 저장하기 위한 리스트
    parent_list[1] = 1

    while queue:
        cur = queue.popleft()
        for neighbor in adj_list[cur]:
            if parent_list[neighbor] == 0: ## parent_list의 i번째 위치가 0이면 이전에 방문한 적이 없다는 것이므로 큐에 삽입.
                parent_list[neighbor] = cur
                queue.append(neighbor)

    for idx in range(2, num_nodes+1):
        print(parent_list[idx])
    
if __name__ == "__main__":
    solution1()