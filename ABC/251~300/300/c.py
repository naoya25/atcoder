def main():
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    n = min(h, w)
    size = {2 * i + 1: 0 for i in range(1, n + 1)}

    for k in sorted(size.keys(), reverse=True):
        for i in range(max(0, h - k + 1)):
            for j in range(max(0, w - k + 1)):
                judge = is_cross([row[j : j + k] for row in grid[i : i + k]], k)
                if judge:
                    for r in range(i, i + k):
                        for c in range(j, j + k):
                            if r - i == c - j or r - i + c - j == k - 1:
                                grid[r][c] = "."
                    size[k] += 1
    print(*size.values())

    return


def is_cross(grid, l):
    if not (len(grid) == l and len(grid[0]) == l):
        return False

    for r in range(l):
        for c in range(l):
            if r == c or r + c == l - 1:
                if grid[r][c] != "#":
                    return False
    else:
        return True


if __name__ == "__main__":
    main()
