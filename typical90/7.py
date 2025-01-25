import bisect


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    q = int(input())
    for _ in range(q):
        b = int(input())
        idx = bisect.bisect_left(a, b)
        if idx == 0:
            print(abs(a[0] - b))
        elif idx == n:
            print(abs(a[-1] - b))
        else:
            print(min(abs(a[idx] - b), abs(a[idx - 1] - b)))

    return


if __name__ == "__main__":
    main()
