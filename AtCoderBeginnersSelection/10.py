s = input()
words = "dream dreamer erase eraser".split()

while len(s) > 0:
    judge = True
    for word in words:
        if s.endswith(word):
            judge = False
            s = s[: -len(word)]
    if judge:
        break
if len(s) == 0:
    print("YES")
else:
    print("NO")

# 別解
# s = input().replace('eraser', '').replace('erase', '').replace('dreamer', '').replace('dream', '')
# print('YES' if s == '' else 'NO')

# 別解(2)
# import re

# s = input()
# if re.compile(r"^(?:dream(?:er)?|eraser?)+$").search(s):
#     print("YES")
# else:
#     print("NO")
