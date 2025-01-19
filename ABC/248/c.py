def main():
    n, m, k = map(int, input().split())
    mod = 998244353

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(k + 1):
            if dp[i][j] == 0:
                continue
            for l in range(1, m + 1):
                if j + l <= k:
                    dp[i + 1][j + l] += dp[i][j]

    print(sum(dp[-1]) % mod)
    return


if __name__ == "__main__":
    main()
