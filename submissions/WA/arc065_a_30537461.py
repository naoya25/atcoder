# URL: https://atcoder.jp/contests/abs/submissions/30537461
# Language: Python (3.8.2)

# submitted code
S = str(input())
for i in range(len(S)):
    if S[:7] == 'dreamer':
        S = S[7:]
    elif S[:5] == 'dream':
        S = S[5:]
    elif S[:6] == 'eraser':
        S = S[6:]
    elif S[:5] == 'erase':
        S = S[5:]
    elif S == '':
        print('YES')
        break
    else:
        print('NO')
        break