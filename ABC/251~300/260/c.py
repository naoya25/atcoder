def main():
    n, x, y = map(int, input().split())
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = 1

    for i in range(n - 1):
        dp[i + 1][0] += dp[i][0]
        dp[i][1] += dp[i][0] * x

        dp[i + 1][0] += dp[i][1]
        dp[i + 1][1] += dp[i][1] * y

    print(dp[n - 1][1])
    return


if __name__ == "__main__":
    main()
