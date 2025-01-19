# URL: https://atcoder.jp/contests/abs/submissions/30550345
# Language: Python (3.8.2)

# submitted code
s = str(input()) #sを取得
while True:
    if s[-5:] == 'dream': #sの末尾にdreamが入ってたら消してsに再代入
        s = s[:-5]
    elif s[-7:] == 'dramer': #同じ
        s = s[:-7]
    elif s[-5:] == 'erase': #同じ
        s = s[:-5]
    elif s[-6:] == 'eraser': #同じ
        s = s[:-6]
    else: #末尾にどの文字列も入ってないときwhileループ終了
        break
if s == '': #sが全て消えてたら
    print('YES')
else: #sに1文字でも残ってたら
    print('NO')