def main():
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]

    for r in range(h):
        for c in range(w - 1):
            if grid[r][c] == "T" and grid[r][c + 1] == "T":
                grid[r][c] = "P"
                grid[r][c + 1] = "C"
    for r in grid:
        print("".join(r))
    return


if __name__ == "__main__":
    main()
