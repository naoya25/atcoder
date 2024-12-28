def main():
    h, w, x, y = map(int, input().split())
    grid = [input() for _ in range(h)]
    t = input()

    direction = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

    x -= 1
    y -= 1

    c = set()

    for ti in t:
        dx, dy = direction[ti]
        nx, ny = x + dx, y + dy

        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != "#":
            x, y = nx, ny

            if grid[x][y] == "@":
                c.add((x, y))

    print(x + 1, y + 1, len(c))


if __name__ == "__main__":
    main()
