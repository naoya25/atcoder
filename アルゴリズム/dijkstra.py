import heapq


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))  # 頂点の重み
    graph = [[] for _ in range(n)]  # 各頂点から繋がってる頂点と辺の重み
    for _ in range(m):
        u, v, b = map(int, input().split())
        graph[u - 1].append((v - 1, b))
        graph[v - 1].append((u - 1, b))
    # print(graph)

    # ダイクストラ
    min_heap = [(a[0], 0)]  # 未確定の候補地(最小重み(未確定ではあるが),現在の頂点)
    dist = [float("inf")] * n  # 頂点ごとの最短経路
    dist[0] = a[0]
    visited = [False] * n  # 確定した頂点

    while min_heap:
        nd, u = heapq.heappop(min_heap) # 重みが最小のものを選ぶ(確定する)

        if visited[u]:
            continue
        visited[u] = True

        # 繋がってる頂点全部試す
        for v, w in graph[u]:
            # より短ければ更新
            if not visited[v] and dist[v] > nd + w + a[v]:
                dist[v] = nd + w + a[v]
                heapq.heappush(min_heap, (dist[v], v))

    print(*dist[1:])
    return


if __name__ == "__main__":
    main()
