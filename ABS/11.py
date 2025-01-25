n = int(input())

bt, bx, by = 0, 0, 0
for _ in range(n):
    t, x, y = map(int, input().split())
    dt = t - bt
    dl = abs(x - bx) + abs(y - by)
    if not (dt >= dl and dt % 2 == dl % 2):
        print("No")
        exit()
    bt, bx, by = t, x, y

print("Yes")
