n = int(input())
arr = list(map(int, input().split()))

count = 0
while all(i % 2 == 0 for i in arr):
    arr = list(map(lambda x: x // 2, arr))
    count += 1

print(count)
