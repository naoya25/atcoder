def main():
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if grid[i][j] == ".":
                continue
            black_count = 0
            if i - 1 >= 0 and grid[i - 1][j] == "#":
                black_count += 1
            if i + 1 < h and grid[i + 1][j] == "#":
                black_count += 1
            if j - 1 >= 0 and grid[i][j - 1] == "#":
                black_count += 1
            if j + 1 < w and grid[i][j + 1] == "#":
                black_count += 1

            if black_count not in [2, 4]:
                print("No")
                return

    print("Yes")

    return


if __name__ == "__main__":
    main()
