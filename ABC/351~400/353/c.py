def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    ans = sum(a) * (n - 1)
    count = 0
    j = n - 1
    for i in range(n - 1):
        while j >= 0 and a[i] + a[j] >= 10**8:
            j -= 1
        count += n - max(i, j) - 1
    print(ans - count * (10**8))


if __name__ == "__main__":
    main()
