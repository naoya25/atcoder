# URL: https://atcoder.jp/contests/abc408/submissions/66357650
# id: 66357650
# epoch_second: 1748698250
# problem_id: abc408_e
# contest_id: abc408
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 0.0
# length: 782
# result: TLE
# execution_time: 3449


# submitted code
from collections import deque


def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    queue = deque()
    queue.append((1, 0, set([1])))  # 頂点, コスト, visited

    ans = float("inf")

    while queue:
        v, cost, visited = queue.popleft()

        if v == n:
            ans = min(ans, cost)
            continue

        for nv, w in graph[v]:
            new_cost = cost | w
            if new_cost < ans and nv not in visited:
                queue.append((nv, new_cost, visited | set([nv])))

    print(ans)
    return


if __name__ == "__main__":
    main()
