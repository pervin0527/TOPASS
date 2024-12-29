import sys

def main():
    n = int(sys.stdin.readline())
    numbers = [0] * 10001

    ## 숫자 등장횟수 저장.
    for _ in range(n):
        v = int(sys.stdin.readline())
        numbers[v] += 1

    ## index i는 수열의 각 원소.
    ## 원소 i가 몇 번 등장했는지는 배열의 i번째 값.
    for i in range(len(numbers)):
        for _ in range(numbers[i]):
            print(i)

if __name__ == "__main__":
    main()
