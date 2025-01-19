from collections import deque


def bfs(graph, start):
    dist = [-1] * len(graph)
    dist[start] = 0
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

    return dist


def main():
    n, k = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        graph[a].append(b)
        graph[b].append(a)

    v = list(map(lambda x: int(x) - 1, input().split()))
    dist_from_first = bfs(graph, v[0])

    # 遠い頂点
    farthest_vertex = v[0]
    for vertex in v:
        if dist_from_first[vertex] > dist_from_first[farthest_vertex]:
            farthest_vertex = vertex
    dist_from_farthest = bfs(graph, farthest_vertex)

    # 遠い頂点
    diameter_end = v[0]
    for vertex in v:
        if dist_from_farthest[vertex] > dist_from_farthest[diameter_end]:
            diameter_end = vertex

    # 5. 直径の長さ + 1が最小の部分木の頂点数
    min_vertices = dist_from_farthest[diameter_end] + 1
    print(max(k, min_vertices))
    # print(min_vertices)


if __name__ == "__main__":
    main()
