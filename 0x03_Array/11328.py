import sys
input = sys.stdin.readline

def str_to_list(x):
    ## a : 97 ~ z : 122
    arr = [0] * 26
    for s in x :
        idx = ord(s) - 97
        arr[idx] += 1

    return arr

def solution():
    n = int(input().strip())
    
    for _ in range(n):
        s1, s2 = input().strip().split()
        # s1 = str_to_list(s1)
        # s2 = str_to_list(s2)

        s1 = sorted(s1)
        s2 = sorted(s2)
        
        if s1 == s2:
            print("Possible")
        else:
            print("Impossible")
        
if __name__ == "__main__":
    solution()