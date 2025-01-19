def main():
    n = int(input())
    a = list(map(int, input().split()))

    dp = [[0, 0] for _ in range(n)]  # 偶奇
    dp[0][1] = a[0]

    for i in range(1, n):
        for j in range(2):
            p1 = dp[i - 1][j]  # 倒さない
            if j == 0:
                p2 = dp[i - 1][(j + 1) % 2] + 2 * a[i]  # 倒してかつ偶数
                dp[i][j] = max(p1, p2)
            else:
                p2 = dp[i - 1][(j + 1) % 2] + a[i]  # 倒したが奇数
                dp[i][j] = max(p1, p2)

    print(max(dp[-1]))


if __name__ == "__main__":
    main()
