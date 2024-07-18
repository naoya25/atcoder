def main():
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]

    directions = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}
    visited = [[False] * w for _ in range(h)]
    visited[0][0] = True
    nr, nc = 0, 0
    while 0 <= nr < h and 0 <= nc < w:
        s = grid[nr][nc]
        dr, dc = directions[s]

        if 0 <= nr + dr < h and 0 <= nc + dc < w:
            nr += dr
            nc += dc
            if visited[nr][nc]:
                print(-1)
                return
            visited[nr][nc] = True
        else:
            print(nr + 1, nc + 1)
            return

    return


if __name__ == "__main__":
    main()
