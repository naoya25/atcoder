import heapq


def main():
    n, m = map(int, input().split())
    graph = {i + 1: [] for i in range(n)}
    roads = [0] * (m + 1)
    for i in range(m):
        a, b, c = map(int, input().split())
        roads[i + 1] = c
        graph[a].append((c, i + 1, b))  # 距離、道路番号、行き先
        graph[b].append((c, i + 1, a))

    # print(graph)

    p_queue = [(0, 1)]  # 距離、現在地
    visited = [False] * (n + 1)
    l = [float("inf")] * (n + 1)
    use_road = [0] * (n + 1)

    while p_queue:
        w, s = heapq.heappop(p_queue)
        if visited[s]:
            continue
        visited[s] = True

        for nw, road_i, ns in graph[s]:
            if not visited[ns] and l[ns] > nw + w:
                l[ns] = nw + w
                use_road[ns] = road_i
                heapq.heappush(p_queue, (nw + w, ns))

    print(*list(set(use_road[2:])))
    return


if __name__ == "__main__":
    main()
