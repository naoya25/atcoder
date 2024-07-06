def main():
    n = int(input())
    m = 998244353

    dp = [[0] * 9 for _ in range(n)]
    dp[0] = [1] * 9

    for i in range(1, n):
        for j in range(9):
            dp[i][j] = dp[i - 1][j]
            if j - 1 >= 0:
                dp[i][j] += dp[i - 1][j - 1]
            if j + 1 < 9:
                dp[i][j] += dp[i - 1][j + 1]
            dp[i][j] %= m

    print(sum(dp[-1]) % m)

    return


if __name__ == "__main__":
    main()
