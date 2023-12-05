import sys

num_scores = int(input())
scores = list(map(int, sys.stdin.readline().rstrip().split()))

max_score = max(scores)
sum_score = 0
for score in scores:
    sum_score += (score / max_score * 100)

avg = sum_score / num_scores
print(avg)