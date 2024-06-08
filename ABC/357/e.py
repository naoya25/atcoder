class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
            self.size[root_x] += self.size[root_y]
        return True


def main():
    n = int(input())
    a = list(map(lambda x: int(x) - 1, input().split()))
    # print(a)
    ans = n

    uf = UnionFind(n)
    for i, ai in enumerate(a):
        uf.union(i, ai)

    ans = 0
    for i in range(n):
        if uf.find(i) == i:
            size = uf.size[i]
            ans += size * (size - 1) // 2
    print(ans)

    return


if __name__ == "__main__":
    main()
