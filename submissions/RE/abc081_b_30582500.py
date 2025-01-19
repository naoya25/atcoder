# URL: https://atcoder.jp/contests/abs/submissions/30582500
# Language: Python (3.8.2)

# submitted code
N = int(input())
x_list = [list(map(int, input().split())) for _ in range(N)]
judge = 'Yes'
if x_list[0][0] - (x_list[0][1] + x_list[0][2]) < 0 or (x_list[0][0] - (x_list[0][1] + x_list[0][2])) % 2 != 0:
    judge = 'No'
for j in range(1,N):
    num = (x_list[j][0] - x_list[j-1][0]) - (x_list[j][1] - x_list[j-1][1]) - (x_list[j][2] - x_list[j-1][2])
    if num < 0 or num % 2 != 0:
        judge = 'No'
print(judge)