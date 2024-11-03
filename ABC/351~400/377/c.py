def main():
    n, m = map(int, input().split())
    cannot_places = set()
    directions = [
        (-1, 2),
        (-1, -2),
        (1, 2),
        (1, -2),
        (2, -1),
        (2, 1),
        (-2, -1),
        (-2, 1),
    ]
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        cannot_places.add((a, b))
        for dx, dy in directions:
            nx, ny = a + dx, b + dy
            if 0 <= nx < n and 0 <= ny < n:
                cannot_places.add((nx, ny))
    print(n * n - len(cannot_places))
    return


if __name__ == "__main__":
    main()
