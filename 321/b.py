n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(101):
  judge = sorted(a + [i])
  if sum(judge[1:-1]) >= x:
    print(i)
    exit()
print(-1)
