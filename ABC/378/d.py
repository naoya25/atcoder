def main():
    h, w, k = map(int, input().split())
    grid = [list(input().strip()) for _ in range(h)]
    ans = 0

    for r in range(h):
        for c in range(w):
            if grid[r][c] == ".":
                ans += dfs(r, c, k, h, w, grid)

    print(ans)


def dfs(r, c, k, h, w, grid):
    stack = [(r, c, k, {(r, c)})]
    count = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while stack:
        cr, cc, remaining_moves, path_visited = stack.pop()

        if remaining_moves == 0:
            count += 1
            continue

        for dr, dc in directions:
            nr, nc = cr + dr, cc + dc
            if (
                0 <= nr < h
                and 0 <= nc < w
                and grid[nr][nc] == "."
                and (nr, nc) not in path_visited
            ):
                new_visited = path_visited | {(nr, nc)}
                stack.append((nr, nc, remaining_moves - 1, new_visited))

    return count


if __name__ == "__main__":
    main()
