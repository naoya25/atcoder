from collections import deque


def main():
    n, m = map(int, input().split())
    graph = [{} for _ in range(n)]
    x = [0] * n
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = w
        graph[v][u] = -w
    # print(graph)

    queue = deque()
    visited = [False] * n

    for start in range(n):
        if visited[start]:
            continue
        queue.append((start, 0))

        while queue:
            current, xi = queue.popleft()

            if visited[current]:
                continue

            visited[current] = True

            for neighbor, weight in graph[current].items():
                if not visited[neighbor]:
                    queue.append((neighbor, xi + weight))
                    x[neighbor] = xi + weight

    if max(x) > 10**18:
        dx = 10**18 - max(x)
        x = [xi - dx for xi in x]
        print(*x)
    elif min(x) < -(10**18):
        dx = -(10**18) - min(x)
        x = [xi + dx for xi in x]
        print(*x)
    else:
        print(*x)


if __name__ == "__main__":
    main()
