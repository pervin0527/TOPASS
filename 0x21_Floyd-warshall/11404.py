import sys
input = sys.stdin.readline

def solution():
    cities = int(input())
    buses = int(input())

    adj_matrix = [[float('inf')] * cities for _ in range(cities)]

    ## A에서 A로 가는 비용을 0으로 처리
    for i in range(cities):
        adj_matrix[i][i] = 0

    ## A에서 B로가는 비용 입력.
    for _ in range(buses):
        start, end, cost = map(int, input().strip().split())
        # 각 경로의 최소 비용을 인접 행렬에 입력한다.
        adj_matrix[start-1][end-1] = min(adj_matrix[start-1][end-1], cost)

    for k in range(cities):
        for st in range(cities):
            for en in range(cities):
                k_cost = adj_matrix[st][k] + adj_matrix[k][en]
                if adj_matrix[st][en] > k_cost:
                    adj_matrix[st][en] = k_cost

    # 결과 출력
    for i in range(cities):
        for j in range(cities):
            if adj_matrix[i][j] == float('inf'):
                print(0, end=' ')
            else:
                print(adj_matrix[i][j], end=' ')
        print()
    

if __name__ == "__main__":
    solution()