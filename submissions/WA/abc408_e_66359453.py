# URL: https://atcoder.jp/contests/abc408/submissions/66359453
# id: 66359453
# epoch_second: 1748698560
# problem_id: abc408_e
# contest_id: abc408
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 0.0
# length: 701
# result: WA
# execution_time: 516


# submitted code
import heapq


def main() -> None:
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
        g[v].append((u, w))

    INF = 1 << 60
    dist = [INF] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)]

    while pq:
        cost, v = heapq.heappop(pq)
        if cost > dist[v]:
            continue
        if v == n:
            print(cost)
            return
        for nv, w in g[v]:
            nc = cost | w
            if nc < dist[nv]:
                dist[nv] = nc
                heapq.heappush(pq, (nc, nv))


if __name__ == "__main__":
    main()
