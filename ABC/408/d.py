def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        calc(n, s)

    return


def calc(n, s):
    ones = s.count("1")
    if ones == 0 or ones == n:
        print(0)
        return
    best = 0
    cur = 0
    for ch in s:
        cur = max(0, cur + (1 if ch == "1" else -1))
        best = max(best, cur)

    print(ones - best)


if __name__ == "__main__":
    main()
