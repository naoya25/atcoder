def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    if k % 2 == 0:
        for i in range(k // 2):
            ans += a[2 * i + 1] - a[2 * i]
    else:
        l = k // 2
        b = [0] * (l + 1)
        for i in range(l):
            b[0] += a[2 * (i + 1)] - a[2 * i + 1]
        for i in range(l):
            b[i + 1] = b[i] - (a[2 * (i + 1)] - a[2 * i + 1]) + (a[2 * i + 1] - a[2 * i])
        ans = min(b)
    print(ans)


if __name__ == "__main__":
    main()
