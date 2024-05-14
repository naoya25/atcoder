import sys
import string
from collections import deque, defaultdict


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
        self.sizes = [1] * n

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])  # 経路圧縮
            return self.parents[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return

        # Union by Rank
        if self.ranks[root_x] < self.ranks[root_y]:
            self.parents[root_x] = root_y
            self.sizes[root_y] += self.sizes[root_x]
        else:
            self.parents[root_y] = root_x
            self.sizes[root_x] += self.sizes[root_y]
            if self.ranks[root_x] == self.ranks[root_y]:
                self.ranks[root_x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    # 親一覧
    def get_roots(self):
        roots = set()
        for i in range(len(self.parents)):
            root = self.find(i)
            roots.add(root)
        return roots

    def size(self, x):
        return self.sizes[self.find(x)]


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
    ls = lambda: list(input())
    lls = lambda n: [ls() for _ in range(n)]
    fli = lambda n: sum(lli(n), [])
    inc = lambda x: x + 1
    dec = lambda x: x - 1
    pe = lambda x: print(x, end=" ")
    pf = lambda x: print(x, flush=True)
    pn = lambda x: print(*x, sep="\n")
    INF = float("inf")
    dd = defaultdict()
    dir8 = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]  # 8方
    dir4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 4方

    h, w = mi()
    grid = lls(h)

    uf = UnionFind(h * w)
    dots = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] == ".":
                dots += 1
                continue

            for dr, dc in dir8:
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == "#":
                    uf.union(r * w + c, nr * w + nc)

    pf(len(uf.get_roots()) - dots)


if __name__ == "__main__":
    main()
    # python main.py < input.txt
