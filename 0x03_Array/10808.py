"""
https://www.acmicpc.net/problem/10808

알파벳 소문자로만 이루어진 단어 S가 입력되었을 때 각 알파벳이 단어에 몇 개가 포함되어 있는지 구해라.
"""
from string import ascii_lowercase

alphabets = list(ascii_lowercase)
count_dict = {}
for alphabet in alphabets:
    count_dict[alphabet] = 0

vocab = input()
for v in vocab:
    count_dict[v] += 1

for v in list(count_dict.values()):
    print(v, end=" ")