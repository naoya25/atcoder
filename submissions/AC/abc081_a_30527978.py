# URL: https://atcoder.jp/contests/abs/submissions/30527978
# Language: Python (3.8.2)

# submitted code
s = list(input()) #1と0からなる整数をlistとして受け取る
ans = 0
for i in s: #受け取った整数を一桁づつansに足してく
    ans += int(i) #listは基本strとして取り出されてるっぽいからintに変換
print(ans)