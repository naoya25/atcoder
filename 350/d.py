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

    def get_roots(self):
        roots = set()
        for i in range(len(self.parents)):
            root = self.find(i)
            roots.add(root)
        return roots

    def size(self, x):
        return self.sizes[self.find(x)]


def main():
    n, m = map(int, input().split())
    uf = UnionFind(n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        uf.union(a, b)

    group_set = uf.get_roots()
    friend_count = 0
    for g in group_set:
        friend_count += calc_friends(uf.size(g))
    print(friend_count - m)


def calc_friends(num):
    return int(num * (num - 1) / 2)


if __name__ == "__main__":
    main()
