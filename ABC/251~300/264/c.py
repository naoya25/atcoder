from itertools import combinations


def main():
    h1, w1 = map(int, input().split())
    grid1 = [list(map(int, input().split())) for _ in range(h1)]
    h2, w2 = map(int, input().split())
    grid2 = [list(map(int, input().split())) for _ in range(h2)]

    dh, dw = h1 - h2, w1 - w2
    if dh < 0 or dw < 0:
        print("No")
        return

    for rs in combinations(range(h1), dh):
        for cs in combinations(range(w1), dw):
            new_grid = []
            for r in range(h1):
                if r in rs:
                    continue
                row = [grid1[r][c] for c in range(w1) if c not in cs]
                new_grid.append(row)

            if grid2 == new_grid:
                print("Yes")
                return
    print("No")
    return


if __name__ == "__main__":
    main()
