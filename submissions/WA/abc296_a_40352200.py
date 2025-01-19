# URL: https://atcoder.jp/contests/abc296/submissions/40352200
# Language: Python (3.8.2)

# submitted code
n = int(input())
s = str(input())

judge = "Yes"
if s[0] == "F":
    a = "F"
else:
    a = "F"
for i in s:
    if i != a:
        judge = "No"
    if a == "F":
        a = "M"
    else:
        a = "F"
print(judge)