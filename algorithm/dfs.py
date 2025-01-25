def dfs(grid):
    visited = [[False] * (w + 1) for _ in range(h + 1)]
    stack = [(0, 0, 0)]
    visited[0][0] = True

    while stack:
        r, c, t = stack.pop()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] - t > 0:
                if (nr, nc) == (y - 1, x - 1):
                    return True
                visited[nr][nc] = True
                stack.append((nr, nc, t + 1))
    return False


if __name__ == "__main__":
    h, w, y, x = map(int, input().split())
    f = [list(map(int, input().split())) for _ in range(h)]

    print("YES" if dfs(f) else "NO")
