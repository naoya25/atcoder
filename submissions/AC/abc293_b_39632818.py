# URL: https://atcoder.jp/contests/abc293/submissions/39632818
# Language: Python (3.8.2)

# submitted code
n = int(input())
p_list = list(map(int, input().split()))

for i in p_list:
    if i != False:
        p_list[i-1] = False
for i in range(n):
    if p_list[i] != False:
        p_list[i] = i +1
ans_list = list(set(p_list))[1:]
print(len(ans_list))
print(*ans_list)