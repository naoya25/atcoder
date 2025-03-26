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
            return False

        # Union by Rank
        if self.ranks[root_x] < self.ranks[root_y]:
            self.parents[root_x] = root_y
            self.sizes[root_y] += self.sizes[root_x]
        else:
            self.parents[root_y] = root_x
            self.sizes[root_x] += self.sizes[root_y]
            if self.ranks[root_x] == self.ranks[root_y]:
                self.ranks[root_x] += 1
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def get_roots(self):
        """全頂点について find した結果の代表の集合を返す"""
        roots = set()
        for i in range(len(self.parents)):
            roots.add(self.find(i))
        return roots

    def size(self, x):
        return self.sizes[self.find(x)]


def main():
    n, m = map(int, input().split())
    uf = UnionFind(n)

    edges = []
    extra_edge_ids = []

    for i in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        edges.append((a, b))
        if not uf.union(a, b):
            extra_edge_ids.append(i)

    roots = list(uf.get_roots())
    c = len(roots)

    if c == 1:
        print(0)
        return

    root_to_id = {}
    for idx, r in enumerate(roots):
        root_to_id[r] = idx

    comp_id = [0] * n
    for i in range(n):
        comp_id[i] = root_to_id[uf.find(i)]

    uf_comp = UnionFind(c)
    operations = []

    target_comps = list(range(1, c))

    p = 0
    for t in target_comps:
        while uf_comp.find(0) != uf_comp.find(t):
            e_idx = extra_edge_ids[p]
            p += 1
            a, b = edges[e_idx]
            old_server = b + 1
            new_server = roots[t] + 1
            operations.append((e_idx + 1, old_server, new_server))

            uf_comp.union(0, t)

    print(len(operations))
    for op in operations:
        print(*op)


if __name__ == "__main__":
    main()
