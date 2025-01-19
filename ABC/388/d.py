def main():
    n = int(input())
    a = list(map(int, input().split()))

    c = [0] * n
    d = [0] * (n + 1)

    for i in range(n):
        if i != 0:
            c[i] = c[i - 1] + d[i]
            a[i] += c[i]

        give = min(a[i], (n - i - 1))
        a[i] -= give

        d[i + 1] += 1
        d[i + give + 1] -= 1

    print(*a)
    return


if __name__ == "__main__":
    main()
