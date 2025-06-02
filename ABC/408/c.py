def main():
    n, m = map(int, input().split())
    l = [0] * m
    r = [0] * m
    for i in range(m):
        l[i], r[i] = map(int, input().split())

    l.sort()
    r.sort()
    walls = [0] * (n + 2)
    for i in range(m):
        walls[l[i]] += 1
        walls[r[i] + 1] -= 1

    for i in range(1, n + 1):
        walls[i] += walls[i - 1]

    print(min(walls[1 : n + 1]))

    return


if __name__ == "__main__":
    main()
