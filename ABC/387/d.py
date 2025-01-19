from collections import deque


def main():
    h, w = map(int, input().split())
    grid = [input() for _ in range(h)]

    start, goal = None, None

    for i in range(h):
        for j in range(w):
            if grid[i][j] == "S":
                start = (i, j)
            elif grid[i][j] == "G":
                goal = (i, j)

    if start is None or goal is None:
        print(-1)
        return

    queue = deque()
    queue.append((start[0], start[1], None, 0))

    visited = set()
    visited.add((start[0], start[1], None))

    vertical_dirs = [(1, 0), (-1, 0)]
    horizontal_dirs = [(0, 1), (0, -1)]

    while queue:
        r, c, was_vertical, dist = queue.popleft()

        if (r, c) == goal:
            print(dist)
            return

        if was_vertical is None or was_vertical is False:
            for dr, dc in vertical_dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] != "#":
                    if (nr, nc, True) not in visited:
                        visited.add((nr, nc, True))
                        queue.append((nr, nc, True, dist + 1))

        if was_vertical is None or was_vertical is True:
            for dr, dc in horizontal_dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] != "#":
                    if (nr, nc, False) not in visited:
                        visited.add((nr, nc, False))
                        queue.append((nr, nc, False, dist + 1))

    print(-1)


if __name__ == "__main__":
    main()
