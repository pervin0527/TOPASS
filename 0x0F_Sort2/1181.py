if __name__ == "__main__":
    n = int(input())
    vocabs = []
    for _ in range(n):
        v = input()
        if v not in vocabs:
            vocabs.append(v)

    vocabs.sort(key=lambda x: (len(x), x))
    for item in vocabs:
        print(item)