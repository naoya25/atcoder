from collections import deque


def main():
    h, w = map(int, input().split())
    grid = [input() for _ in range(h)]

    stack = deque([(0, 0, 0)])
    visited = [[False] * w for _ in range(h)]
    visited[0][0] = True

    ans = float("inf")

    while stack:
        x, y, cells = stack.popleft()
        if x == h - 1 and y == w - 1:
            ans = min(ans, cells)
            continue

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < h
                and 0 <= ny < w
                and grid[nx][ny] == "."
                and not visited[nx][ny]
            ):
                visited[nx][ny] = True
                stack.append((nx, ny, cells + 1))

    if ans == float("inf"):
        print("Unreachable")
    else:
        print(ans)


if __name__ == "__main__":
    main()
