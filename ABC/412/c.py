from bisect import bisect_right


def solve(dominoes):
    start, end = dominoes[0], dominoes[-1]

    if start >= end:
        print(2)
        return

    mids = [x for x in sorted(dominoes) if start <= x <= end]

    current = start
    ans = 1

    while current < end:
        idx = bisect_right(mids, 2 * current) - 1

        if mids[idx] == current:
            print(-1)
            return

        current = mids[idx]
        ans += 1
    print(ans)


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))
        solve(s)


if __name__ == "__main__":
    main()
