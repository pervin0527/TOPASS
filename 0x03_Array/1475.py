"""
https://www.acmicpc.net/problem/1475

한 세트가 0부터 9까지 숫자가 하나씩 들어 있을 때 입력된 방번호를 만들 수 있는 세트의 수.
6은 9로, 9는 6으로 뒤집어서 사용이 가능하다.
"""

room = input()
numbers = [0] * 10

for r in room:
    r = int(r)

    if r == 6 and numbers[r] > 0:
        if numbers[9] == numbers[r] - 1:
            numbers[9] += 1
        else:
            numbers[r] += 1

    elif r == 9 and numbers[r] > 0:
        if numbers[6] == numbers[r] - 1:
            numbers[6] += 1
        else:
            numbers[r] += 1
    else:
        numbers[r] += 1

print(max(numbers))