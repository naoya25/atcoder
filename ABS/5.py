
a = int(input())  # 500円玉
b = int(input())  # 100円玉
c = int(input())  # 50円玉
x = int(input())

count = 0
for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c + 1):
            if 500 * i + 100 * j + 50 * k == x:
                count += 1
print(count)

# 別解
# a = int(input())
# b = int(input())
# c = int(input())
# x = int(input())

# count = 0
# for i in range(a + 1):
#   for j in range(b + 1):
#     k = (x - (500 * i + 100 * j))
#     if 0 <= k // 50 <= c and k % 50 == 0:
#       count += 1
# print(count)
