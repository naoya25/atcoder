import bisect


def main():
    n = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        j = bisect.bisect_left(a, a[i] * 2, i + 1)
        cnt += n - j

    print(cnt)
    return


if __name__ == "__main__":
    main()
