def main():
    grid = []
    for _ in range(8):
        grid.append(list(input()))

    rows, columns = 0, 0
    for r in grid:
        if r.count("#") == 0:
            rows += 1
    for c in range(8):
        column = [grid[r][c] for r in range(8)]
        if column.count("#") == 0:
            columns += 1
    print(rows * columns)
    return


if __name__ == "__main__":
    main()
