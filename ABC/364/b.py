def main():
    h, w = map(int, input().split())
    si, sj = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    x = input()

    directions = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}

    for xi in x:
        di, dj = directions[xi]
        ni, nj = si + di, sj + dj
        if 0 < ni <= h and 0 < nj <= w and grid[ni - 1][nj - 1] == ".":
            si, sj = ni, nj

    print(si, sj)
    return


if __name__ == "__main__":
    main()
