def main():
    x1, y1, x2, y2 = map(int, input().split())
    ds = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    p1 = [(x1 + dx, y1 + dy) for dx, dy in ds]

    for dx, dy in ds:
        if (x2 + dx, y2 + dy) in p1:
            print("Yes")
            return
    else:
        print("No")


if __name__ == "__main__":
    main()
