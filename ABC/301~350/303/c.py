def main():
    n, m, h, k = map(int, input().split())
    s = input()
    items = set()
    for _ in range(m):
        x, y = map(int, input().split())
        items.add(f"{x}_{y}")
    # print(items)
    directions = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}
    px, py = 0, 0
    for si in s:
        dx, dy = directions[si]
        px += dx
        py += dy
        h -= 1
        if h < 0:
            print("No")
            return
        if h < k and f'{px}_{py}' in items:
            h = k
            items.remove(f'{px}_{py}')
    print("Yes")
    return


if __name__ == "__main__":
    main()
