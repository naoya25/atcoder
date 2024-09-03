def main():
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    dp = [0] * n

    for i in range(2, n):
        if a[i - 2] - a[i - 1] == a[i - 1] - a[i]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 0

        count += dp[i]

    count += n + (n - 1)

    print(count)

if __name__ == "__main__":
    main()
