def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a_sum = [0] * (n - m + 1)
    a_sum[0] = sum(a[:m])
    for i in range(1, n - m + 1):
        a_sum[i] = a_sum[i - 1] + a[m + i - 1] - a[i - 1]

    dp = [0] * (n - m + 1)
    dp[0] = sum(a[i] * (i + 1) for i in range(m))
    for i in range(1, n - m + 1):
        dp[i] = dp[i - 1] - a_sum[i - 1] + a[i + m - 1] * m

    print(max(dp))
    return


if __name__ == "__main__":
    main()
