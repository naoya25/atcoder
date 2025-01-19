import bisect


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(n - 1):
        if a[i] < a[i + 1]:
            a[i + 1] = a[i]
    a.sort()
    min_a = a[0]

    for j in range(m):
        idx = bisect.bisect_right(a, b[j])
        if b[j] < min_a:
            print(-1)
            continue
        print(n - idx + 1)


if __name__ == "__main__":
    main()
