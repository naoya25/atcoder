# URL: https://atcoder.jp/contests/abc408/submissions/66351962
# id: 66351962
# epoch_second: 1748697278
# problem_id: abc408_e
# contest_id: abc408
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 0.0
# length: 847
# result: WA
# execution_time: 466


# submitted code
import heapq


def main():
    n, m = map(int, input().split())

    # 1-idx
    graph = {i: {} for i in range(1, n + 1)}
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u][v] = w
        graph[v][u] = w

    INF = 1e18
    dist = {i: INF for i in range(1, n + 1)}
    dist[1] = 0

    pq = [(0, 1)]  # (OR値, 頂点)

    while pq:
        cost, current = heapq.heappop(pq)

        if cost != dist[current]:
            continue
        if current == n:
            break

        for neighbor, weight in graph[current].items():
            new_cost = cost | weight  # OR
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

    print(dist[n])


if __name__ == "__main__":
    main()
