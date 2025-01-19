import sys
sys.setrecursionlimit(10**7)


def main():
    N, M, K = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # クラスカル法、MSTを構築
    edges.sort(key=lambda x: x[0])
    par = list(range(N + 1))
    rank = [0] * (N + 1)

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return False
        if rank[a] < rank[b]:
            a, b = b, a
        par[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1
        return True

    mst = [[] for _ in range(N + 1)]
    for w, u, v in edges:
        if union(u, v):
            mst[u].append((v, w))
            mst[v].append((u, w))

    # LCA
    LOG = (N + 1).bit_length()
    parent = [[-1] * (N + 1) for _ in range(LOG)]
    max_edge_up = [[0] * (N + 1) for _ in range(LOG)]
    depth = [0] * (N + 1)

    def dfs(cur, p, d):
        depth[cur] = d
        for nxt, w in mst[cur]:
            if nxt == p:
                continue
            parent[0][nxt] = cur
            max_edge_up[0][nxt] = w
            dfs(nxt, cur, d + 1)

    dfs(1, -1, 0)

    for k in range(1, LOG):
        for v in range(1, N + 1):
            if parent[k - 1][v] == -1:
                parent[k][v] = -1
                max_edge_up[k][v] = max_edge_up[k - 1][v]
            else:
                pv = parent[k - 1][v]
                parent[k][v] = parent[k - 1][pv]
                max_edge_up[k][v] = max(max_edge_up[k - 1][v], max_edge_up[k - 1][pv])

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        for i in range(LOG):
            if diff & (1 << i):
                u = parent[i][u]
        if u == v:
            return u
        for i in reversed(range(LOG)):
            if parent[i][u] != parent[i][v]:
                u = parent[i][u]
                v = parent[i][v]
        return parent[0][u]

    def get_max_edge(u, dist):
        ret = 0
        for i in range(LOG):
            if dist & (1 << i):
                ret = max(ret, max_edge_up[i][u])
                u = parent[i][u]
        return ret

    def get_max_on_path(x, y):
        r = lca(x, y)
        return max(
            get_max_edge(x, depth[x] - depth[r]), get_max_edge(y, depth[y] - depth[r])
        )

    # 貪欲法
    A.sort()
    B.sort()

    ans = 0
    for i in range(K):
        ans += get_max_on_path(A[i], B[i])

    print(ans)


if __name__ == "__main__":
    main()
