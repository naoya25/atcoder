def main():
    n = int(input())
    if n == 0:
        print("#")
        return

    l = 3**n
    carpet = [["#"] * l for _ in range(l)]

    for k in range(1, n + 1):
        bl = 3 ** (k - 1)
        for i in range(0, l, 3 * bl):
            for j in range(0, l, 3 * bl):
                carpet = fill_white(i + bl, j + bl, bl, carpet)

    for r in carpet:
        print("".join(r))

    return


def fill_white(x, y, size, carpet):
    for i in range(size):
        for j in range(size):
            carpet[x + i][y + j] = "."
    return carpet


if __name__ == "__main__":
    main()
