from collections import deque


def main():
    h, w, k = map(int, input().split())
    goals = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]

    INF = 10**18

    grid = [[INF] * w for _ in range(h)]
    mn1 = [[INF] * w for _ in range(h)]
    mn2 = [[INF] * w for _ in range(h)]

    max_d = 4 * (h + w)
    bucket = [deque() for _ in range(max_d)]

    for r, c in goals:
        grid[r][c] = 0
        bucket[0].append((r, c))

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for d in range(max_d):
        bq = bucket[d]
        while bq:
            i, j = bq.popleft()
            if grid[i][j] != d:
                continue

            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if not (0 <= ni < h and 0 <= nj < w):
                    continue

                old2 = mn2[ni][nj]
                # 最小値更新
                if d < mn1[ni][nj]:
                    mn2[ni][nj] = mn1[ni][nj]
                    mn1[ni][nj] = d
                elif d < mn2[ni][nj]:
                    mn2[ni][nj] = d

                if mn2[ni][nj] != old2:
                    tmp = mn2[ni][nj] + 1
                    if tmp < grid[ni][nj]:
                        grid[ni][nj] = tmp
                        if tmp < max_d:
                            bucket[tmp].append((ni, nj))

    ans = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] < INF:
                ans += grid[i][j]
    print(ans)


if __name__ == "__main__":
    main()
