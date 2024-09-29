def recursive(n, s, e, t, arr):
    """
    n : 원판의 개수
    s : 현재 원판이 위치한 시작 기둥 번호.
    t : 중간에 사용할 임시 기둥 번호.
    e : 원판을 옮길 목적 기둥 번호.
    """
    if n == 1:
        arr.append((s, e))
        return
    
    recursive(n-1, s, t, e, arr)
    arr.append((s, e))
    recursive(n-1, t, e, s, arr)

def main():
    n = int(input().rstrip())
    
    moves = []
    recursive(n, 1, 3, 2, moves)

    print(len(moves))
    for move in moves:
        print(move[0], move[1])

if __name__ == "__main__":
    main()