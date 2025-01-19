# URL: https://atcoder.jp/contests/abs/submissions/30531184
# Language: Python (3.8.2)

# submitted code
N = int(input())
A_list = list(map(int, input().split()))
Finish = False
count = 0
while Finish == False:
    for i in range(N): 
        if A_list[i] % 2 == 0:
            A_list[i] = A_list[i] / 2
        else:
            Finish = True
    count += 1
print(count-1)