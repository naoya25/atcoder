# URL: https://atcoder.jp/contests/abc259/submissions/41690967
# Language: Python (3.8.2)

# submitted code
N, M, X, T, D = map(int, input().split())

print(T if M >= X else T - (X - M) * D)