# URL: https://atcoder.jp/contests/abc296/submissions/40354923
# Language: Python (3.8.2)

# submitted code
N, M = map(int,input().split())
 
from math import sqrt, floor
ans = inf = 1 << 60
for a in range(1, min(N, floor(sqrt(M+0.01)))+20):
  b = ((-M) // a)
  b *= -1
  
  if not(1 <= a <= N) or not(1 <= b <= N) or not(a * b >= M): continue
  c = b * a
  ans = min(ans, c)
  
print(ans if ans != inf else -1)