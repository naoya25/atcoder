import heapq


def main():
    h, w, x = map(int, input().split())
    p, q = map(lambda x: int(x) - 1, input().split())
    grid = [list(map(int, input().split())) for _ in range(h)]

    T = grid[p][q]  # 高橋くんの強さ

    visited = [[False] * w for _ in range(h)]  # 高橋くんの占有領域
    visited[p][q] = True

    frontier = []  # 優先度付きキュー
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for di, dj in directions:
        ni, nj = p + di, q + dj
        if 0 <= ni < h and 0 <= nj < w:
            heapq.heappush(frontier, (grid[ni][nj], ni, nj))

    while frontier:
        # 最弱スライム
        strength, i, j = heapq.heappop(frontier)
        if visited[i][j]:
            continue
        if strength * x < T:
            visited[i][j] = True
            T += strength
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj]:
                    heapq.heappush(frontier, (grid[ni][nj], ni, nj))
        else:
            break

    print(T)


if __name__ == "__main__":
    main()
