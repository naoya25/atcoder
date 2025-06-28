import sys

sys.setrecursionlimit(10**7)


def hungarian(a):
    """
    a: n×n のコスト行列 (0-indexed)
    return: (min_cost, match)
      - min_cost は最小合計コスト
      - match[i] = j は「左側 i が右側 j に対応付いた」ことを表す
    時間計算量 O(n^3)
    """
    n = len(a)
    INF = 10**18

    # ポテンシャルとマッチング情報 (1-indexed で扱う)
    u = [0] * (n + 1)
    v = [0] * (n + 1)
    p = [0] * (n + 1)
    way = [0] * (n + 1)

    for i in range(1, n + 1):
        p[0] = i
        j0 = 0
        minv = [INF] * (n + 1)
        used = [False] * (n + 1)

        # augmenting path
        while True:
            used[j0] = True
            i0 = p[j0]
            delta = INF
            j1 = 0
            for j in range(1, n + 1):
                if used[j]:
                    continue
                # コストの差分
                cur = a[i0 - 1][j - 1] - u[i0] - v[j]
                if cur < minv[j]:
                    minv[j] = cur
                    way[j] = j0
                if minv[j] < delta:
                    delta = minv[j]
                    j1 = j
            # ポテンシャル更新
            for j in range(n + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta
            j0 = j1
            if p[j0] == 0:
                break

        # augment
        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break

    # マッチング結果を 0-indexed の配列に変換
    match = [-1] * n
    for j in range(1, n + 1):
        if p[j] > 0:
            match[p[j] - 1] = j - 1

    # -v[0] が最小コストの合計
    return -v[0], match


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    # 隣接を bool で管理
    adj = [[False] * N for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u][v] = adj[v][u] = True

    # cost[i][j] = 0 if (i,j)∈E(G), =1 otherwise, =INF if i==j
    INF = 10**9
    cost = [[INF] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            cost[i][j] = 0 if adj[i][j] else 1

    # 有向完全グラフ上の最小コスト巡回被覆を求める
    C, match = hungarian(cost)

    # 最終的な操作回数
    # 追加 = C
    # 削除 = M - (使われた既存辺数) = M - (N - C)
    ans = M - N + 2 * C
    print(ans)


if __name__ == "__main__":
    main()
