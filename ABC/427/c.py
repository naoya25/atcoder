def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, input().split())
        edges.append((u, v))

    ans = m

    for bit in range(1 << n):
        delete_count = 0
        for u, v in edges:
            # 頂点uとvが同じ色（bit上の同じビット値）なら削除対象
            if ((bit >> u) & 1) == ((bit >> v) & 1):
                delete_count += 1
        ans = min(ans, delete_count)

    print(ans)


if __name__ == "__main__":
    main()
