def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dp1 = [False] * n
    dp2 = [False] * n

    dp1[0], dp2[0] = True, True

    for i in range(1, n):
        if dp1[i - 1]:
            if abs(a[i - 1] - a[i]) <= k:
                dp1[i] = True
            if abs(a[i - 1] - b[i]) <= k:
                dp2[i] = True
        if dp2[i - 1]:
            if abs(b[i - 1] - a[i]) <= k:
                dp1[i] = True
            if abs(b[i - 1] - b[i]) <= k:
                dp2[i] = True

    print("Yes" if dp1[n - 1] or dp2[n - 1] else "No")


if __name__ == "__main__":
    main()
