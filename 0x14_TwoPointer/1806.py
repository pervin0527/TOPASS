N, S = map(int, input().split())
sequence = list(map(int, input().split()))

start = 0
end = 0
min_length = float('inf')
current_sum = 0

while True:
    if current_sum >= S:
        min_length = min(min_length, end - start)
        current_sum -= sequence[start]
        start += 1
    elif end == N:
        break
    else:
        current_sum += sequence[end]
        end += 1

if min_length == float('inf'):
    print(0)
else:
    print(min_length)