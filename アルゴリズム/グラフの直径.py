from collections import defaultdict, deque


def bfs(start, graph):
    n = len(graph)
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])

    farthest_node = start
    max_dist = 0

    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)
                if dist[neighbor] > max_dist:
                    max_dist = dist[neighbor]
                    farthest_node = neighbor

    return farthest_node, max_dist


def main():
    n = int(input())
    graph = defaultdict(list)

    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 1 からの最遠の点
    u, _ = bfs(1, graph)

    # u からの最遠の点
    _, diameter = bfs(u, graph)

    # print("グラフの直径:", diameter)
    print(diameter + 1)


if __name__ == "__main__":
    main()
