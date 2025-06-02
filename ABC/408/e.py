def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    stack = []
    stack.append((1, 0, set([1])))  # 頂点, コスト, visited

    ans = float("inf")

    while stack:
        v, cost, visited = stack.pop()

        if v == n:
            ans = min(ans, cost)
            continue

        for nv, w in graph[v]:
            new_cost = cost | w
            if new_cost < ans and nv not in visited:
                stack.append((nv, new_cost, visited | set([nv])))

    print(ans)
    return


if __name__ == "__main__":
    main()
