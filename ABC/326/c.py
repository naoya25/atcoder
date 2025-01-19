import sys
import string
from collections import deque, defaultdict


def main():
    input = lambda: sys.stdin.readline().rstrip()
    int1 = lambda x: int(x) - 1
    ii = lambda: int(input())
    i1 = lambda: int1(input())
    mi = lambda: map(int, input().split())
    mi1 = lambda: map(int1, input().split())
    li = lambda: list(mi())
    li1 = lambda: list(mi1())
    lli = lambda n: [li() for _ in range(n)]
    fli = lambda n: sum(lli(n), [])
    inc = lambda x: x + 1
    dec = lambda x: x - 1
    pe = lambda x: print(x, end=" ")
    pf = lambda x: print(x, flush=True)
    pn = lambda x: print(*x, sep="\n")
    INF = float("inf")
    dd = defaultdict()

    n, m = mi()
    a = li()
    keys = list(set(a))
    keys.sort()
    for ai in a:
        if ai in dd.keys():
            dd[ai] += 1
        else:
            dd[ai] = 1

    j = 0
    ans = 0
    num = 0
    for i in keys:
        while j < len(keys) and keys[j] - i < m:
            num += dd[keys[j]]
            j += 1
        ans = max(ans, num)
        num -= dd[i]
    pf(ans)


if __name__ == "__main__":
    main()
    # python main.py < input.txt
