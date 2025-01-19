def main():
    n, x, y = map(int, input().split())
    graph = {i + 1: [] for i in range(n)}
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # dfsでノード1を探す
    parent = [-1] * (n + 1)
    visited = [False] * (n + 1)
    stack = [x]
    visited[x] = True

    while stack:
        c = stack.pop()
        for to in graph[c]:
            if not visited[to]:
                visited[to] = True
                parent[to] = c
                stack.append(to)
    # print(parent)

    # y→x
    path = []
    cur = y
    while cur != -1:
        path.append(cur)
        cur = parent[cur]

    print(*path[::-1])


if __name__ == "__main__":
    main()
