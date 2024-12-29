## input() 대신 sys.stdin.readline()
## print() 대신 sys.stdout.write()

import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

    arr.sort()
    sys.stdout.write("\n".join(map(str, arr)) + "\n")

if __name__ == "__main__":
    main()
