# URL: https://atcoder.jp/contests/abc408/submissions/66354076
# id: 66354076
# epoch_second: 1748697636
# problem_id: abc408_e
# contest_id: abc408
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 0.0
# length: 668
# result: WA
# execution_time: 629


# submitted code
import heapq


def main():
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    INF = 1e18
    dist = [INF] * (n + 1)
    dist[1] = 0

    pq = [(0, 1)]

    while pq:
        cost, v = heapq.heappop(pq)
        if cost != dist[v]:
            continue
        for nv, w in graph[v]:
            nc = cost | w
            if nc < dist[nv]:
                dist[nv] = nc
                heapq.heappush(pq, (nc, nv))

    print(dist[n])


if __name__ == "__main__":
    main()
