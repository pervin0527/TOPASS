def func(n, start=0):
    under_lines = '____' * start
    print(f'{under_lines}"재귀함수가 뭔가요?"')

    if start == n:
        print(f'{under_lines}"재귀함수는 자기 자신을 호출하는 함수라네"')
    else:
        print(f'{under_lines}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print(f'{under_lines}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print(f'{under_lines}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        func(n, start+1)

    print(f'{under_lines}라고 답변하였지.')


if __name__ == '__main__':
    n = int(input())
    print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
    func(n)

# def recur_func(tmp, n):
#     indent = "____" * tmp
#     print(f'{indent}"재귀함수가 뭔가요?"')

#     if tmp == n:
#         print(f'{indent}"재귀함수는 자기 자신을 호출하는 함수라네"')
#         print(f'{indent}라고 답변하였지.')
#         return

#     print(f'{indent}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
#     print(f'{indent}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
#     print(f'{indent}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')

#     recur_func(tmp + 1, n)
#     print(f'{indent}라고 답변하였지.')

# def main():
#     n = int(input().rstrip())

#     print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
#     recur_func(0, n)

# if __name__ == "__main__":
#     main()
