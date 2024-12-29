def rotate(paper, r, c):
    tmp = [[0] * r for _ in range(c)]
    
    for i in range(r):
        for j in range(c):
            tmp[j][r-1-i] = paper[i][j]
    
    return tmp, c, r


def pastable(note, paper, x, y, r, c):
    ## 하나의 이중 for문을 사용한다면 스티커의 일부를 붙이는 문제가 발생하기 때문에 두 개로 분리함.
    for i in range(r):
        for j in range(c):
            if note[x+i][y+j] == 1 and paper[i][j] == 1:
                return note, False
    
    for i in range(r):
        for j in range(c):
            if paper[i][j] == 1:
                note[x+i][y+j] = 1
    
    return note, True


def main():
    n, m, k = map(int, input().split())
    note = [[0] * m for _ in range(n)] ## 노트북
    
    for _ in range(k):
        r, c = map(int, input().split())
        paper = [list(map(int, input().split())) for _ in range(r)] ## 스티커
        
        for _ in range(4): ## 4방향 내에서 붙일 수 있는가
            is_paste = False
            for x in range(n - r + 1): ## 노트북 내에서 영역 탐색.
                if is_paste: 
                    break
                for y in range(m - c + 1):
                    note, result = pastable(note, paper, x, y, r, c)
                    if result: ## 붙일 수 있다.
                        is_paste = True
                        break
            if is_paste: 
                break
            paper, r, c = rotate(paper, r, c)
    
    cnt = sum(row.count(1) for row in note)
    print(cnt)

if __name__ == "__main__":
    main()
