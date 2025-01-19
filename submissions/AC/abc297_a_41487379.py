# URL: https://atcoder.jp/contests/abc297/submissions/41487379
# Language: Python (3.8.2)

# submitted code
n, d = map(int, input().split())
clicks = list(map(int, input().split()))

f = True
for i in range(n-1):
    if clicks[i + 1] - clicks[i] <= d:
        print(clicks[i + 1])
        f = False
        break

if f:
    print(-1)