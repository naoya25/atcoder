import bisect
from collections import defaultdict


def main():
    n, m, x, y = map(int, input().split())
    x, y = x - 1, y - 1

    houses_rows = defaultdict(list)
    houses_cols = defaultdict(list)

    for _ in range(n):
        hx, hy = map(lambda x: int(x) - 1, input().split())
        houses_rows[hy].append(hx)
        houses_cols[hx].append(hy)

    for row in houses_rows:
        houses_rows[row].sort()
    for col in houses_cols:
        houses_cols[col].sort()

    direction = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}
    visited_houses = set()

    for _ in range(m):
        d, c = input().split()
        c = int(c)
        dx, dy = direction[d]

        if dx != 0:  # 水平移動
            cx = x
            nx = x + dx * c

            if cx < nx:
                low = cx + 1
                high = nx
            else:
                low = nx
                high = cx - 1

            if y in houses_rows:
                xs = houses_rows[y]

                start_idx = bisect.bisect_left(xs, low)
                end_idx = bisect.bisect_right(xs, high)

                for visited_x in xs[start_idx:end_idx]:
                    visited_houses.add((visited_x, y))
            x = nx

        else:  # 垂直移動
            col = x
            current_y = y
            new_y = y + dy * c

            if current_y < new_y:
                low = current_y + 1
                high = new_y
            else:
                low = new_y
                high = current_y - 1

            if col in houses_cols:
                ys = houses_cols[col]

                start_idx = bisect.bisect_left(ys, low)
                end_idx = bisect.bisect_right(ys, high)

                for visited_y in ys[start_idx:end_idx]:
                    visited_houses.add((col, visited_y))
            y = new_y

    print(x + 1, y + 1, len(visited_houses))


if __name__ == "__main__":
    main()
