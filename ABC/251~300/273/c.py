from collections import defaultdict


def main():
    n = int(input())
    a = list(map(int, input().split()))
    arr = sorted(list(set(a)))

    dn = defaultdict(int)
    dd = defaultdict(int)
    for i in range(1, n + 1):
        dn[a[i - 1]] += 1
    for i in range(1, len(arr) + 1):
        dd[len(arr) - i] = arr[i - 1]

    ans = [dn[dd[i]] for i in range(n)]
    for a in ans:
        print(a)

    return


if __name__ == "__main__":
    main()
