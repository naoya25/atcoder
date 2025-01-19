# URL: https://atcoder.jp/contests/abs/submissions/30530097
# Language: Python (3.8.2)

# submitted code
N = int(input())
A_list = list(input().split())
Finish = False
count = 0
while Finish == False:
    for i in range(N):
        if int(A_list[i]) % 2 == 0:
            A_list[i] = int(A_list[i]) / 2
        else:
            Finish = True
    count += 1
print(count-1)