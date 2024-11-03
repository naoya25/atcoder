from collections import defaultdict


def main():
    n = int(input())
    a = list(map(int, input().split()))

    dd = defaultdict(lambda: -1)
    for i in range(n):
        print(dd[a[i]])
        dd[a[i]] = i + 1

    return


if __name__ == "__main__":
    main()
