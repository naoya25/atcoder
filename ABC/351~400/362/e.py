def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = 998244353

    ans = [0] * 5
    dk = max(a) - min(a)

    # dp[i][j][k] i: 埋めた桁数, j: 1つ前のindex, k: 2つ前のindex
    dp = []
    for _ in range(n + 1):
        dp.append([[0] * n for _ in range(n)])

    # i == 1を埋める
    for j in range(n):
        dp[1][j][0] += 1
    # i == 2を埋める
    for j in range(n):
        for k in range(j):
            dp[2][j][k] = 1

    for i in range(2, n + 1):
        for j in range(n):
            for k in range(n):
                if dp[i][j][k] == 0:
                    continue
                for ni in range(j + 1, n):
                    if a[ni] - a[j] == a[j] - a[k]:
                        dp[i + 1][ni][j] += dp[i][j][k]

    print(*[sum(sum(r, [])) % m for r in dp[1:]])
    return


if __name__ == "__main__":
    main()
