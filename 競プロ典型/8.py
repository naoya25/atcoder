def main():
    n = int(input())
    s = input()
    t = "atcoder"
    mod = 10**9 + 7

    dp = [[0] * (len(t) + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(len(t) + 1):
            dp[i + 1][j] += dp[i][j]

            if j < len(t) and s[i] == t[j]:
                dp[i + 1][j + 1] += dp[i][j]

    print(dp[n][len(t)] % mod)

    return


if __name__ == "__main__":
    main()
