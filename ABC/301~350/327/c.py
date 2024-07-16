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

    a = "".join(map(str, fli(9)))

    for i in range(9):
        ss = a[i * 9 : (i + 1) * 9]
        for j in range(1, 10):
            if ss.count(str(j)) > 1:
                pf("No")
                return
    # 縦
    for i in range(9):
        ss = [a[i % 9 + 9 * j] for j in range(9)]
        for j in range(1, 10):
            if ss.count(str(j)) > 1:
                pf("No")
                return
    # 3 x 3
    for i in range(9):
        ss = [a[i // 3 * 27 + i % 3 * 3 + j // 3 * 9 + j % 3] for j in range(9)]
        for j in range(1, 10):
            if ss.count(str(j)) > 1:
                pf("No")
                return
    pf("Yes")
    return


if __name__ == "__main__":
    main()
    # python main.py < input.txt
