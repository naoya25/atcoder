# URL: https://atcoder.jp/contests/abs/submissions/30531498
# Language: Python (3.8.2)

# submitted code
N = int(input())
a_list = list(map(int, input().split()))
a_list = sorted(a_list, reverse=True)
AricePoint = 0
BobPoint = 0
for i in range(N):
    if i % 2 == 0:
        AricePoint += a_list[i]
    else:
        BobPoint += a_list[i]
print(AricePoint - BobPoint)