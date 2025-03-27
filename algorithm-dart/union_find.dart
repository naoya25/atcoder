class UnionFind {
  List<int> parent;
  List<int> rank;

  UnionFind(int n)
    : parent = List.generate(n, (i) => i),
      rank = List.filled(n, 0);

  int find(int x) {
    if (parent[x] != x) {
      parent[x] = find(parent[x]);
    }
    return parent[x];
  }

  void unite(int x, int y) {
    int rootX = find(x);
    int rootY = find(y);

    if (rootX == rootY) return;

    if (rank[rootX] < rank[rootY]) {
      parent[rootX] = rootY;
    } else {
      parent[rootY] = rootX;
      if (rank[rootX] == rank[rootY]) {
        rank[rootX]++;
      }
    }
  }

  bool same(int x, int y) {
    return find(x) == find(y);
  }
}
