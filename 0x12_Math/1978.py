import sys
import math

def is_prime(n : int):
    if n == 1:
        return False
    
    i = 2
    while (i**2) <= n:
    # while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    
    return True

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input().rstrip())
    numbers = list(map(int, input().rstrip().split()))

    prime_numbers = 0
    for number in numbers:
        if is_prime(number):
            prime_numbers += 1

    print(prime_numbers)
