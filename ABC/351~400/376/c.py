from sortedcontainers import SortedList


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(reverse=True)
    sorted_b = SortedList(b)

    count = 0
    ans = 0

    for ai in a:
        pos = sorted_b.bisect_left(ai)
        if pos < len(sorted_b):
            sorted_b.pop(pos)
        else:
            count += 1
            ans = ai
            if count > 1:
                print(-1)
                return

    print(ans)


if __name__ == "__main__":
    main()
