# URL: https://atcoder.jp/contests/abc293/submissions/39623084
# Language: Python (3.8.2)

# submitted code
s = str(input())
t = []
for i in range(0, len(s), 2):
  t.append(s[i+1])
  t.append(s[i])
print("".join(t))