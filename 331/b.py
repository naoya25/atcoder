n, s, m, l = map(int, input().split())
ans = float("inf")

for a in range(100):
    for b in range(100):
        c = max(-(-(n - (6 * a + 8 * b)) // 12), 0)
        if 6 * a + 8 * b + 12 * c >= n:
            ans = min(ans, s * a + m * b + l * c)

print(ans)
