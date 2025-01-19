# URL: https://atcoder.jp/contests/abc293/submissions/39621152
# Language: Python (3.8.2)

# submitted code
s = str(input())

for i in range(0, len(s), 2):
  a = s[i]
  b = s[i+1]
  s[i] = b
  s[i+1] = a
 print(s)