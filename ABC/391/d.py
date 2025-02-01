import bisect


def solve():
    n, w = map(int, input().split())
    blocks = []
    for i in range(n):
        x, y = map(int, input().split())
        blocks.append((x, y, i))

    cols = [[] for _ in range(w + 1)]
    for x, y, idx in blocks:
        cols[x].append((y, idx))

    rank_arr = [0] * n
    col_sizes = [0] * (w + 1)
    sorted_y = [None] * (w + 1)
    for col in range(1, w + 1):
        if cols[col]:
            cols[col].sort(key=lambda p: p[0])
            col_sizes[col] = len(cols[col])
            sorted_y[col] = [p[0] for p in cols[col]]
            for i, (y, idx) in enumerate(cols[col]):
                rank_arr[idx] = i + 1
        else:
            col_sizes[col] = 0
            sorted_y[col] = []

    R_max = min(col_sizes[1:])

    B = []  # B[r] = 列 x の r 番目に小さい y の最大値
    for r in range(1, R_max + 1):
        current = 0
        for col in range(1, w + 1):
            if sorted_y[col][r - 1] > current:
                current = sorted_y[col][r - 1]
        B.append(current)

    q = int(input())
    queries = []
    for qi in range(q):
        T, a = map(int, input().split())
        queries.append((T, a - 1, qi))

    block_col = [0] * n
    block_y = [0] * n
    for x, y, idx in blocks:
        block_col[idx] = x
        block_y[idx] = y

    ans = [None] * q
    for T, a, qi in queries:
        r_block = rank_arr[a]
        if R_max == 0:
            ans[qi] = "Yes"
            continue

        m_val = bisect.bisect_right(B, T)
        ans[qi] = "Yes" if r_block > m_val else "No"

    for a in ans:
        print(a)


if __name__ == "__main__":
    solve()
