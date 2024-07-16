from itertools import permutations
from collections import defaultdict


def main():
    n, m = map(int, input().split())
    takahashi, aoki = defaultdict(list), defaultdict(list)
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        takahashi[a].append(b)
        takahashi[b].append(a)
    for _ in range(m):
        c, d = map(lambda x: int(x) - 1, input().split())
        aoki[c].append(d)
        aoki[d].append(c)

    for p in permutations(range(n)):
        if judge(n, p, takahashi, aoki):
            print("Yes")
            return
    print("No")
    return


# def judge(n, p, takahashi, aoki):
#     for i in range(n):
#         for ai in aoki[p[i]]:
#             if p[ai] not in takahashi[i]:
#                 return False
#     return True

def judge(n, p, takahashi, aoki):
    for i in range(n):
        for ai in takahashi[i]:
            if p[ai] not in aoki[p[i]]:
                return False
    return True

if __name__ == "__main__":
    main()
