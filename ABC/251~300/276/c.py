from bisect import bisect_left


def main():
    n = int(input())
    p = list(map(int, input().split()))

    for i in range(1, n):
        if p[-i] < p[-i - 1]:
            break

    arr = p[-i:]
    arr.sort()
    idx = bisect_left(arr, p[-i - 1]) - 1
    p[-i - 1], arr[idx] = arr[idx], p[-i - 1]

    ans = p[:-i] + arr[::-1]
    print(*ans)

    return


if __name__ == "__main__":
    main()
