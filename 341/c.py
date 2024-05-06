def main():
    h, w, n = map(int, input().split())
    t = input()
    grid = [list(input()) for _ in range(h)]

    ans = 0
    for r in range(1, h - 1):
        for c in range(1, w - 1):
            if grid[r][c] == "#":
                continue
            nr, nc = r, c
            for dt in t:
                if dt == "L":
                    nc -= 1
                elif dt == "R":
                    nc += 1
                elif dt == "U":
                    nr -= 1
                elif dt == "D":
                    nr += 1

                if grid[nr][nc] == "#":
                    break

            else:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
