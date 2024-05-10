def main():
    n = int(input())
    a = list(map(int, input().split()))

    d = dict()
    for i, ai in enumerate(a):
        if ai in d.keys():
            d[ai].append(i)
        else:
            d[ai] = [i]

    ans = [0] * n
    now = 0
    for k, v in sorted(d.items(), reverse=True):
        for i in v:
            ans[i] = now
        now += k * len(v)

    print(*ans)


if __name__ == "__main__":
    main()
