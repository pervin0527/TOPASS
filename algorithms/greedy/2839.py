"""
https://www.acmicpc.net/problem/2839

먼저, 주어진 N이 5 또는 3의 배수인지 확인하고 배수인 경우 바로 나눈다.
배수가 아니라면 3과 5의 조합으로 N을 만들 수 있는지 검사한다.
앞서 수행한 두 개의 방식 중 어떤 것에도 해당되지 않는 경우 3과 5로는 해당 수를 표현할 수 없기 때문에 -1을 출력한다.

메모리 : 31120KB, 소요시간 : 44ms
"""

N = int(input())

results = []
if N % 5 == 0:
    results.append(N // 5)

if N % 3 == 0:
    results.append(N // 3)

for num5 in range(1, (N // 5) + 1):
    if (N - 5 * num5) % 3 == 0:
        results.append(num5 + (N - (5 * num5)) // 3)

if results:
    print(min(results))

else:
    print(-1)

"""
좀 더 그리디에 적합한 풀이.
핵심은 for문이 N//5부터 0까지로 반복한다는 점이다.

def min_bags(N):
    for five_kg_bags in range(N // 5, -1, -1):
        remaining_weight = N - (five_kg_bags * 5)

        if remaining_weight % 3 == 0:
            three_kg_bags = remaining_weight // 3
            
            return five_kg_bags + three_kg_bags
        
    return -1

print(min_bags(int(input())))
"""


"""
예전 풀이 방법.
  - 이 방식으로 하면 메모리는 동일하지만 소요 시간이 3684ms로 더 오래 걸린다.
  - 두 번의 for문으로 N을 순회하므로 O(N^2)의 시간 복잡도를 갖는 더 비효율적인 코드다.

N = int(input())
check_list = []

for i in range(N):
    for j in range(N):
        if (i * 5) + (j * 3) == N:
            check_list.append(i + j)

if len(check_list) < 1:
    print(-1)
else:
    print(min(check_list))
"""