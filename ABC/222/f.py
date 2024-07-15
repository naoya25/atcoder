import heapq


def main():
    n = int(input())
    graph = {i + 1: [] for i in range(n)}
    for _ in range(n - 1):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))
    d = [0] + list(map(int, input().split()))
    # print(graph)
    # print(d)

    def dijcstra(start):
        p_heap = [(0, start)]
        visited = [False] * (n + 1)
        l = [float("inf")] * (n + 1)
        l[start] = 0

        while p_heap:
            w, s = heapq.heappop(p_heap)
            if visited[s]:
                continue
            visited[s] = True

            for nw, ns in graph[s]:
                if not visited[ns] and l[ns] > w + nw:
                    l[ns] = w + nw
                    heapq.heappush(p_heap, (w + nw, ns))

        ml, mj = 0, 0
        for j in range(1, n + 1):
            if ml < l[j]:
                ml = l[j]
                mj = j
        return ml + d[mj]

    for i in range(1, n + 1):
        ans = dijcstra(i)
        print(ans)

    return


if __name__ == "__main__":
    main()
