from sortedcontainers import SortedList


def main():
    n = int(input())
    s = SortedList()
    for _ in range(n):
        q = list(map(int, input().split()))
        if q[0] == 1:
            s.add(q[1])
        elif q[0] == 2:
            for _ in range(min(q[2], s.count(q[1]))):
                s.remove(q[1])
        else:
            print(s[-1] - s[0])
    return


if __name__ == "__main__":
    main()
