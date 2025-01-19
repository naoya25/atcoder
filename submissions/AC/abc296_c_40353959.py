# URL: https://atcoder.jp/contests/abc296/submissions/40353959
# Language: Python (3.8.2)

# submitted code
n, x = map(int, input().split())
a_list = set(list(map(int, input().split())))
b_list = set(map(lambda y: y + x, a_list))
if x == 0:
    print("Yes")
elif len(a_list & b_list) != 0:
    print('Yes')
else:
    print("No")