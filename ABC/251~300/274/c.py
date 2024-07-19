def main():
    n = int(input())
    a = list(map(int, input().split()))

    dp = [0] * (2 * n + 2)
    for i in range(n):
        dp[2 * (i + 1)] = dp[a[i]] + 1
        dp[2 * (i + 1) + 1] = dp[a[i]] + 1

    for i in dp[1:]:
        print(i)
    return


if __name__ == "__main__":
    main()
