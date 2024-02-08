import sys

def main(n):
    """
    방 번호의 각 수를 일단 리스트에 모두 +1씩해서 저장.
    그런 다음, arr[6]과 arr[9]의 수를 모두 더하고, 2로 나눈 몫을 구한다.
    arr[6]에는 몫을 저장하고 arr[9]에는 몫 - arr[6]으로 나머지 값을 저장한다.
    """
    arr = [0 for i in range(10)]

    for x in list(str(n)):
        arr[int(x)] += 1

    t69 = arr[6] + arr[9] ## arr[6] = 3, arr[9] = 0 일 때 t69=3
    arr[6] = t69 // 2 ## t69 // 2 = 1 이므로 틀렸지만, 세트의 수만 구하면 되기 때문에 정답임.
    arr[9] = t69 - arr[6]

    return max(arr)


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(main(n))
