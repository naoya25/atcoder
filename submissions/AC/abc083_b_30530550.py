# URL: https://atcoder.jp/contests/abs/submissions/30530550
# Language: Python (3.8.2)

# submitted code
N,A,B = map(int,input().split())
ans = 0
for i in range(1,N+1):
    sum = 0
    for j in range(len(str(i))):
        sum += int(str(i)[j])
    if A <= sum <= B:
        ans += i
print(ans)