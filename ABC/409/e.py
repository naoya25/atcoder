def main() -> None:
    n = int(input())
    x = list(map(int, input().split()))  # 電子陽子の数

    # 0-index
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        g[u - 1].append((v - 1, w))
        g[v - 1].append((u - 1, w))

    ans = 0
    visited = [False] * n
    subtotal = [0] * n  # 各ノードの部分木の合計を保持

    stack = [(0, -1, 0)]  # (現在ノード, 親ノード, フェーズ: 0=前処理, 1=後処理)
    path_stack = []  # 経路記憶

    while stack:
        v, p, phase = stack.pop()
        if phase == 0:
            visited[v] = True
            stack.append((v, p, 1))
            for nv, w in g[v]:
                if nv == p:
                    continue
                stack.append((nv, v, 0))
                path_stack.append((v, nv, w))
        else:
            subtotal[v] = x[v]
            for nv, w in g[v]:
                if nv == p:
                    continue
                subtotal[v] += subtotal[nv]
                ans += abs(subtotal[nv]) * w

    print(ans)


if __name__ == "__main__":
    main()
