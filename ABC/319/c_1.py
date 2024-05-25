data = [0] * 9
from itertools import permutations

data[0], data[1], data[2] = map(int, input().split())
data[3], data[4], data[5] = map(int, input().split())
data[6], data[7], data[8] = map(int, input().split())

judge = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
cnt = 0
total = 0
open = list(range(0, 9))

for perm in permutations(open):
    total += 1
    bool = False
    for a, b, c in judge:
        if data[a] == data[b] and perm[a] < perm[c] and perm[b] < perm[c]:
            bool = True
        if data[b] == data[c] and perm[b] < perm[a] and perm[c] < perm[a]:
            bool = True
        if data[a] == data[c] and perm[a] < perm[b] and perm[c] < perm[b]:
            bool = True
    if not bool:
        cnt += 1

print(cnt / total)
