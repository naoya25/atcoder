n = int(input())
count = 0
st, sx, sy = 0, 0, 0
for i in range(n):
  t, x, y = map(int, input().split())
  if abs(x - sx) + abs(y - sy) <= t - st and (abs(x - sx) + abs(y - sy) - (t - st)) % 2 == 0:
    count += 1
  st, sx, sy = t, x, y
print('Yes' if count == n else 'No')
