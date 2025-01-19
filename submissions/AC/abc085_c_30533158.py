# URL: https://atcoder.jp/contests/abs/submissions/30533158
# Language: Python (3.8.2)

# submitted code
N, Y = map(int, input().split())
liar = True
ans_list = []
for a in range(N+1):
    for b in range(N+1-a):
        if 10000*a + 5000*b + 1000*(N-a-b) == Y:
            ans_list.append(f'{a} {b} {N-a-b}')
            liar = False
        else:
            continue
if liar == True:
    print('-1 -1 -1')
else:
    print(ans_list[0])