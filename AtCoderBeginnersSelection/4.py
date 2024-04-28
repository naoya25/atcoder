def is_even(arr):
    for v in arr:
        if v % 2 != 0:
            return False
    return True

n = int(input())
a_arr = list(map(int, input().split()))

count = 0
while is_even(a_arr):
    for i in range(n):
        a_arr[i] //= 2
    count += 1
print(count)

# 別解
# n = int(input())
# arr = list(map(int, input().split()))

# count = 0
# while all(i % 2 == 0 for i in arr):
#     arr = list(map(lambda x: x // 2, arr))
#     count += 1

# print(count)
