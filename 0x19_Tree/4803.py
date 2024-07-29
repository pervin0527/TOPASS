import sys
input = sys.stdin.readline
from collections import deque

def bfs(tree, start, parents):
    queue = deque([start])
    parents[start] = 1
    
    is_tree = True
    while queue:
        node = queue.popleft() ## 1 --> 3
        for children in tree[node]: ## [2, 3] --> [1, 2]
            if parents[children] == 0:
                queue.append(children)
                parents[children] = node

            ## children이 이전에 방문한 상태이고, children 노드가 현재 탐색 중인 노드의 부모 노드가 아니라면, 이는 현재 탐색 중인 노드와 children 노드 사이에 사이클이 존재한다는 것을 의미
            ## parents[3]은 1이고 children이 1일 때 양방향 연결이므로 트리지만 children이 2일 때 같은 레벨에서 좌우로 연결된 간선이 존재하므로 사이클에 해당.
            elif parents[node] != children:
                is_tree = False
    
    return is_tree

def solution():
    test_cases = []

    while True:
        num_nodes, num_edges = map(int, input().strip().split())

        if num_nodes == 0 and num_edges == 0:
            break
        
        adj_list = [[] for _ in range(num_nodes + 1)]
        for _ in range(num_edges):
            u, v = map(int, input().strip().split())
            adj_list[u].append(v)
            adj_list[v].append(u)

        test_cases.append(adj_list)

    for idx, tree in enumerate(test_cases):
        num_trees = 0
        parents = [0] * len(tree)

        ## 트리에 있는 모든 노드를 탐색.
        for node in range(1, len(tree)):
            if parents[node] == 0:
                if bfs(tree, node, parents):
                    num_trees += 1

        if num_trees == 0:
            print(f'Case {idx + 1}: No trees.')
        elif num_trees == 1:
            print(f'Case {idx + 1}: There is one tree.')
        else:
            print(f'Case {idx + 1}: A forest of {num_trees} trees.')

if __name__ == "__main__":
    solution()
