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
    pe = lambda x: print(x, end=" ")
    pf = lambda x: print(x, flush=True)
    pn = lambda x: print(*x, sep="\n")
    INF = float("inf")
    dd = defaultdict()

    n, q = mi()
    s = input()
    s_sum = [0] * n  # 0~iの範囲にあるペアの数
    count = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            count += 1
        s_sum[i + 1] = count

    for _ in range(q):
        ans = 0
        l, r = mi1()
        pf(s_sum[r] - s_sum[l])


if __name__ == "__main__":
    main()
    # python main.py < input.txt
