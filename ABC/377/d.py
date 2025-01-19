def main():
    n, m = map(int, input().split())

    intervals = [tuple(map(int, input().split())) for _ in range(n)]

    min_right = [m + 1] * (m + 1)

    for l, r in intervals:
        min_right[l] = min(min_right[l], r)

    for i in range(m - 1, 0, -1):
        min_right[i] = min(min_right[i], min_right[i + 1])

    ans = 0
    for l in range(1, m + 1):
        if min_right[l] > m:
            ans += m - l + 1
        else:
            ans += min_right[l] - l

    print(ans)


if __name__ == "__main__":
    main()
