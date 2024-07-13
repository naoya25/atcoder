import heapq


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, b = map(int, input().split())
        graph[u].append((v, b))
        graph[v].append((u, b))

    def dijkstra(start):
        min_heap = [(a[start - 1], start)]
        dist = [float("inf")] * (n + 1)
        dist[start] = a[start - 1]
        visited = [False] * (n + 1)

        while min_heap:
            current_dist, u = heapq.heappop(min_heap)

            if visited[u]:
                continue
            visited[u] = True

            for v, weight in graph[u]:
                if not visited[v] and dist[v] > current_dist + weight + a[v - 1]:
                    dist[v] = current_dist + weight + a[v - 1]
                    heapq.heappush(min_heap, (dist[v], v))

        return dist

    shortest_paths = dijkstra(1)

    ans = [shortest_paths[i] for i in range(2, n + 1)]
    print(*ans)

    return


if __name__ == "__main__":
    main()
