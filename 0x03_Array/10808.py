import sys
input = sys.stdin.readline

def solution():
    check = [0] * 26
    word = input().strip()
    for w in word:
        idx = ord(w) - 97 ## character의 아스키코드를 활용한다.
        check[idx] += 1

    result = ' '.join(map(str, check))
    print(result)

if __name__ == "__main__":
    solution()