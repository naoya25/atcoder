n, a, b = map(int, input().split())
ans = 0
for i in range(1,n+1):
  i_sum = sum(map(int, str(i)))
  if a <= i_sum <= b:
        ans += i
print(ans)
