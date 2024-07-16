def main():
    def dfs(sr, sc, memo):  # スタート位置
        if memo[sr][sc] != -1:
            return memo[sr][sc]

        visited = [[False] * (w + 1) for _ in range(h + 1)]
        stack = [(sr, sc)]
        visited[sr][sc] = True
        while stack:
            r, c = stack.pop()
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            judge = True
            for dr, dc in directions:  # 四方に磁石がある場合
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == "#":
                    judge = False
            if not judge:
                continue
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] == ".":
                    visited[nr][nc] = True
                    stack.append((nr, nc))

        memo[sr][sc] = sum(sum(row) for row in visited)
        return memo[sr][sc]

    h, w = map(int, input().split())
    grid = [input() for _ in range(h)]
    memo = [[-1] * w for _ in range(h)]  # メモ化用の配列
    max_count = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "#":
                continue

            max_count = max(max_count, dfs(i, j, memo))
    print(max_count)


if __name__ == "__main__":
    main()
