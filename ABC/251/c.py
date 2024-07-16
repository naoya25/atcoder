def main():
    n = int(input())
    names = set()
    original = []
    for i in range(1, n + 1):
        s, t = input().split()
        t = int(t)
        if s not in names:
            names.add(s)
            original.append((t, i))
    original.sort(key=lambda x: (x[0], -x[1]))
    print(original[-1][1])
    return


if __name__ == "__main__":
    main()
