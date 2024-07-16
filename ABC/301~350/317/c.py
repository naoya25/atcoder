from collections import defaultdict


def main():
    n, m = map(int, input().split())

    town = {i + 1: [] for i in range(n)}  # 繋がってる街の無向グラフ

    # 2つの町に2通り以上の道路があるパターンってあるんかな

    for _ in range(m):
        a, b, c = map(int, input().split())
        town[a].append([b, c])  # [行き先, 距離]
        town[b].append([a, c])
    # print(town)

    stack = [(i + 1, {i + 1}, 0) for i in range(n)]  # (現在地, 通ったことある町のset, 移動距離)
    ans = 0
    while stack:
        now_t, visited, l = stack.pop()
        ans = max(ans, l)
        for t in town[now_t]:
            if t[0] not in visited:
                stack.append((t[0], visited | {t[0]}, l + t[1]))
    print(ans)
    return


if __name__ == "__main__":
    main()
