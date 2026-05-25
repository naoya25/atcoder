from collections import deque


def main():
    n, m = map(int, input().split())

    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, c = input().split()
        u, v = int(u) - 1, int(v) - 1
        graph[u].append((v, c))
        graph[v].append((u, c))

    # state:
    #   0 = (last=0, prev=0)  スプリント可
    #   1 = (last=0, prev=1)  スプリント不可
    #   2 = (last=1, prev=0)  スプリント不可
    INF = float("inf")
    dist = [[INF] * 3 for _ in range(n)]
    dist[0][0] = 0
    dq = deque([(0, 0, 0)])  # (cost, node, state)

    while dq:
        d, u, s = dq.popleft()
        if d > dist[u][s]:
            continue
        if u == n - 1:
            continue

        for v, c in graph[u]:
            # 通常移動: cost 1, 新stateは last=0, prev=(今のlast)
            new_s_normal = 1 if s == 2 else 0
            nd = d + 1
            if nd < dist[v][new_s_normal]:
                dist[v][new_s_normal] = nd
                dq.append((nd, v, new_s_normal))

            # スプリント: cost 0, c=="R" かつ s==0 のときのみ
            if c == "R" and s == 0:
                new_s_sprint = 2
                if d < dist[v][new_s_sprint]:
                    dist[v][new_s_sprint] = d
                    dq.appendleft((d, v, new_s_sprint))

    print(min(dist[n - 1]))


if __name__ == "__main__":
    main()
