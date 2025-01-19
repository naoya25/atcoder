# URL: https://atcoder.jp/contests/abs/submissions/40351664
# Language: Python (3.8.2)

# submitted code
N = int(input())
all_list = [list(map(int, input().split())) for _ in range(N)]
judge = 'Yes'
 
for j in range(1,N):
    num = (all_list[j][0] - all_list[j-1][0]) - abs(all_list[j][1] - all_list[j-1][1]) - abs(all_list[j][2] - all_list[j-1][2])
    if num < 0 or num % 2 != 0:
        judge = 'No'
print(judge)