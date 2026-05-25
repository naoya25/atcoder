from bisect import bisect_right


def main():
    n, x = map(int, input().split())
    w = list(map(int, input().split()))
    sorted_w = sorted(w)

    ans = []

    for i in range(n):
        idx = bisect_right(sorted_w, x - w[i])

        if w[i] * 2 <= x:
            ans.append(idx - 1)
        else:
            ans.append(idx)

    print(*ans)


if __name__ == "__main__":
    main()
