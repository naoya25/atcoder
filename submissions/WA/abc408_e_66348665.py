# URL: https://atcoder.jp/contests/abc408/submissions/66348665
# id: 66348665
# epoch_second: 1748696720
# problem_id: abc408_e
# contest_id: abc408
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 0.0
# length: 802
# result: WA
# execution_time: 3383


# submitted code
from collections import deque


def main():
    n, m = map(int, input().split())

    # 1-idx
    graph = {i: {} for i in range(1, n + 1)}
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u][v] = w
        graph[v][u] = w

    queue = deque([(1, [1], 0)])
    ans = float("inf")
    while queue:
        current, path, cost = queue.popleft()

        if current == n:
            ans = min(ans, cost)
            continue

        for neighbor, weight in graph[current].items():
            if neighbor not in path:
                new_path = path + [neighbor]
                new_cost = cost | weight  # OR
                queue.append((neighbor, new_path, new_cost))

    print(ans)
    return


if __name__ == "__main__":
    main()
