def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = a + b
    c.sort()

    sa = set(a)
    sb = set(b)
    ans_a = []
    ans_b = []

    for i in range(n + m):
        if c[i] in sa:
            ans_a.append(i + 1)
        else:
            ans_b.append(i + 1)

    print(*ans_a)
    print(*ans_b)
    return


if __name__ == "__main__":
    main()
