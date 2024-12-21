from collections import deque

def main():
    h, w, d = map(int, input().split())
    grid = [list(input().strip()) for _ in range(h)]

    visited = [[False] * w for _ in range(h)]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # BFS
    queue = deque()
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "H":
                queue.append((i, j, 0))
                visited[i][j] = True

    ans = set()

    while queue:
        x, y, depth = queue.popleft()
        ans.add((x, y))
        if depth >= d:
            continue
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w:
                if grid[nx][ny] != "#" and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, depth + 1))

    print(len(ans))


if __name__ == "__main__":
    main()
