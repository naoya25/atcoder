from itertools import combinations


def main():
    h, w, d = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    floors = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] != "#":
                floors.add((r, c))

    ans = 0
    floor_pairs = list(combinations(floors, 2))
    for pair in floor_pairs:
        ans = max(ans, calc_ans(grid, h, w, d, pair))
    print(ans)
    return


def calc_ans(grid, h, w, d, pair):
    floor_count = set()
    for r in range(h):
        for c in range(w):
            if (r, c) not in pair:
                continue
            floor_count.add((r, c))
            for r2 in range(h):
                for c2 in range(w):
                    if (
                        abs(r - r2) + abs(c - c2) <= d
                        and 0 <= r2 < h
                        and 0 <= c2 < w
                        and grid[r2][c2] == "."
                    ):
                        floor_count.add((r2, c2))
    return len(floor_count)


if __name__ == "__main__":
    main()
