# URL: https://atcoder.jp/contests/abs/submissions/30532988
# Language: Python (3.8.2)

# submitted code
N, Y = map(int, input().split())
liar = True
for a in range(N+1):
    for b in range(N+1-a):
        if 10000*a + 5000*b + 1000*(N-a-b) == Y:
            print(f'{a} {b} {N-a-b}')
            liar = False
            break
        else:
            continue
if liar == True:
    print('-1 -1 -1')