import heapq


# 有向グラフの最短経路問題
def main():
    n = int(input())
    graph = {i + 1: [] for i in range(n)}

    for i in range(1, n):
        a, b, x = map(int, input().split())
        graph[i].append((a, i + 1))
        graph[i].append((b, x))

    visited = [False] * (n + 1)  # 確定している箇所
    ans = [float("inf")] * (n + 1)
    p_queue = [(0, 1)]  # コスト, 現在地
    ans[1] = 0  # スタート地点のコストは0

    while p_queue:
        w, s = heapq.heappop(p_queue)
        visited[s] = True

        for nw, ns in graph[s]:
            if not visited[ns] and ans[ns] > w + nw:
                ans[ns] = w + nw
                heapq.heappush(p_queue, (w + nw, ns))

    print(ans[n])


if __name__ == "__main__":
    main()
