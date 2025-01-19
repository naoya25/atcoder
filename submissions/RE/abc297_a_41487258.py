# URL: https://atcoder.jp/contests/abc297/submissions/41487258
# Language: Python (3.8.2)

# submitted code
n, d = map(int, input().split())
clicks = list(map(int, input().split()))
d_clicks = [clicks[i] - clicks[i - 1] for i in range(1, n)]

if min(d_clicks) > d:
    print(-1)
else:
    for i in range(n-1):
        if d_clicks[i] > d:
            continue
        print(clicks[i + 1])
        break