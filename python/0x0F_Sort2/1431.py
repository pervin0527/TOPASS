if __name__ == "__main__":
    n = int(input())
    numbers = [input() for _ in range(n)]

    ## 람다에서 괄호로 묶여 있는게 비교 조건 순위들이다. 1순위가 길이, 2순위가 숫자들의 합, 3순위가 사전 순(숫자가 알파벳보다 낮은 순위)
    ## sum(int(char)) for char in x if char.isdigit() --> 현재의 단어 x의 문자 char이 숫자면 합을 구함.
    ## 만약에 숫자가 포함되지 않은 경우 sum은 0을 반환함.
    sorted_numbers = sorted(numbers, key=lambda x: (len(x), sum(int(char) for char in x if char.isdigit()), x))
    for num in sorted_numbers:
        print(num)