N = int(input())
S = input()
C = [0] + [int(x) for x in input().split()]

dp = [[float('inf')] * 2 for _ in range(N+1)]
dp[0][0] = 0
dp[0][1] = C[1]

for i in range(1, N+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][1] + C[i])
    dp[i][1] = min(dp[i-1][0], dp[i-1][0] + C[i])

print(min(dp[N][0], dp[N][1]))
