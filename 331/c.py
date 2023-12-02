# n = int(input())
# a_list = list(map(int, input().split()))

# print(*[sum(e for e in a_list if e > a) for a in a_list])

import numpy as np

n = int(input())
a_list = np.array(list(map(int, input().split())))

print(*[np.sum(a_list * (a_list > a)) for a in a_list])
