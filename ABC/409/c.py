from collections import Counter


def main() -> None:
    n, L = map(int, input().split())
    d = list(map(int, input().split()))

    if L % 3:
        print(0)
        return

    step = L // 3

    pos = [0] * n
    for i in range(1, n):
        pos[i] = (pos[i - 1] + d[i - 1]) % L

    cnt = Counter(pos)
    seen = set()
    ans = 0

    for p in cnt:
        q = (p + step) % L
        r = (p + 2 * step) % L
        if q in cnt and r in cnt:
            tri = tuple(sorted((p, q, r)))
            if tri not in seen:
                seen.add(tri)
                ans += cnt[p] * cnt[q] * cnt[r]

    print(ans)


if __name__ == "__main__":
    main()
