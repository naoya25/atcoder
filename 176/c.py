n = int(input())

a_list = list(map(int, input().split()))

ans = 0
for i in range(n - 1):
    ans += max(a_list[i] - a_list[i + 1], 0)
    a_list[i + 1] = max(a_list[i], a_list[i + 1])

print(ans)
