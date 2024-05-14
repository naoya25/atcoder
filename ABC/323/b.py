n = int(input())
ans = []
for i in range(n):
    point = list(input()).count('o')
    ans.append([i+1, point])
ans.sort(key=lambda x: [-x[1], x[0]])
print(*[a[0] for a in ans])

"""
n = int(input())
ans = [(i+1, list(input()).count('o')) for i in range(n)]
ans.sort(key=lambda x: (-x[1], x[0]))
print(*[a[0] for a in ans])
"""
