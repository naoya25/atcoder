def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = {i + 1: 0 for i in range(n)}
    f = [[0, i + 1] for i in range(n)]
    for i in range(3 * n):
        cnt[a[i]] += 1
        if cnt[a[i]] == 2:
            f[a[i] - 1][0] = i
    f.sort()
    print(*[e[1] for e in f])
    return


if __name__ == "__main__":
    main()
