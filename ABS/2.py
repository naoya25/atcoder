a, b = map(int, input().split())
volume = a * b
if volume % 2 == 0:
    print("Even")
else:
    print("Odd")

# 別解
# a, b = map(int, input().split())
# print("Odd" if a * b % 2 else "Even")
