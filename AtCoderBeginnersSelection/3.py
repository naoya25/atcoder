s = input()
ans = 0
for c in s:
    if c == '1':
        ans += 1

print(ans)

# 別解
# ans = sum(map(int, list(input())))
# print(ans)

# 別解(2)
# s = input()
# print(s.count('1'))
