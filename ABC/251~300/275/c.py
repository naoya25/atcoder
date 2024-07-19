from itertools import combinations


def main():
    grid = [list(input()) for _ in range(9)]

    p = set()
    for r in range(9):
        for c in range(9):
            if grid[r][c] == "#":
                p.add((r, c))

    ans = 0
    for comb in combinations(p, 4):  # 10^6くらい 最大 81C4
        if is_square(comb):
            ans += 1
    print(ans)
    return


def is_square(points):
    arr = []
    for i in points:
        for j in points:
            if i == j:
                continue
            arr.append(d2(i, j))
    arr.sort()
    return arr[0] == arr[1] == arr[2] == arr[3] and arr[-1] == arr[-2] and arr[0] * 2 == arr[-1]


def d2(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


if __name__ == "__main__":
    main()
