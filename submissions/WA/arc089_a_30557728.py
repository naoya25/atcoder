# URL: https://atcoder.jp/contests/abs/submissions/30557728
# Language: Python (3.8.2)

# submitted code
N = int(input())
x_list = []
for i in range(N):
    x_list.append(list(map(int, input().split())))
judge = 'Yes'
for j in range(N):
    if x_list[j][0] - (x_list[j][1] + x_list[j][2]) >= 0 and (x_list[j][0] - (x_list[j][1] + x_list[j][2])) % 2 == 0:
        continue
    else:
        judge = 'No'
print(judge)