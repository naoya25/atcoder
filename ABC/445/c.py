def main():
    n = int(input())
    # 0-indexed
    a = list(map(lambda x: int(x) - 1, input().split()))
    ans = [-1] * n

    stack = []  # (現在地のindex, たどったルートのindex)

    for i in range(n):
        if a[i] == i:
            ans[i] = i + 1
        else:
            stack.append((i, []))

    # 再起的に親を辿る→mastersに辿り着くorループに入る (DFS)
    # ループに入ったら10**100 % ループの長さ から終着点を求める
    # 途中からループに入る場合もあるか

    while stack:
        now, route = stack.pop()
        if ans[now] != -1:
            for r in route:
                ans[r] = ans[now]
            continue

        if now in route:
            # ループに入った場合
            # mu: ループに入るまでの長さ
            # lam: ループ自体の長さ
            # route の mu + 10**100 % lam の index
            mu = route.index(now)
            lam = len(route) - mu

            ans[now] = route[mu + (10**100 % lam)] + 1
            continue

        stack.append((a[now], route + [now]))

    print(*ans)

    return


if __name__ == "__main__":
    main()
