# URL: https://atcoder.jp/contests/abs/submissions/30538574
# Language: Python (3.8.2)

# submitted code
s = str(input())
while True:
    if s[-5:] == 'dream':
        s = s[:-5]
    elif s[-7:] == 'dramer':
        s = s[:-7]
    elif s[-5:] == 'erase':
        s = s[:-5]
    elif s[-6:] == 'eraser':
        s = s[:-6]
    else:
        break
if s == '':
    print('YES')
else:
    print('NO')