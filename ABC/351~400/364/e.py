def main():
    n, x, y = map(int, input().split())
    a, b = [], []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append((ai, bi))
        b.append((bi, ai))
    a.sort()
    b.sort()
    print(a)
    print(b)

    dishes = [(a[i], b[i]) for i in range(n)]

    dishes.sort(key=lambda x: (x[0] + x[1]))

    total_sweetness = 0
    total_saltiness = 0
    count = 0

    for sweetness, saltiness in dishes:
        if total_sweetness + sweetness > x or total_saltiness + saltiness > y:
            break
        total_sweetness += sweetness
        total_saltiness += saltiness
        count += 1

    print(count)
    return


if __name__ == "__main__":
    main()
