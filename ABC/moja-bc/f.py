from collections import Counter


def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    count_a = Counter(a)
    ans = 0

    for i in range(n):
        for j in range(n):
            target = x - a[i] - a[j]
            ans += count_a[target]

    print(ans)


if __name__ == "__main__":
    main()
