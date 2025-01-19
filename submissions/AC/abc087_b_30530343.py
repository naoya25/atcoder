# URL: https://atcoder.jp/contests/abs/submissions/30530343
# Language: Python (3.8.2)

# submitted code
A = int(input())
B = int(input())
C = int(input())
X = int(input())
count = 0
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            if 500*a + 100*b + 50*c == X:
                count += 1
            else:
                continue
print(count)