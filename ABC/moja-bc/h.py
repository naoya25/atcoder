from collections import deque


def main():
    n, m = map(int, input().split())

    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, c = input().split()
        u, v = int(u) - 1, int(v) - 1
        graph[u].append((v, c))
        graph[v].append((u, c))

    stack = deque([(0, 0, [None, None])])  # (current, cost, route_costs)
    visited = [(False, False, False)] * n  # (01, 10, 11)

    ans = float("inf")

    while stack:
        current, cost, routes = stack.popleft()
        if current == n - 1:
            ans = min(ans, cost)
            continue

        b1, b2 = routes[-1], routes[-2]

        for next_node, c in graph[current]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append((next_node, cost + 1, [routes[-1], 1] if routes else [1]))

                if c == "R" and routes and routes[-1] == 1 and routes[-2] == 1:
                    stack.append((next_node, cost, [routes[-1], 0]))

    print(ans - 1)
    return


if __name__ == "__main__":
    main()
