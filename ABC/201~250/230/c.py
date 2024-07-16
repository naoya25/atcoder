def main():
    n, a, b = map(int, input().split())
    a, b = a - 1, b - 1
    p, q, r, s = map(lambda x: int(x) - 1, input().split())
    grid = [["."] * (s - r + 1) for _ in range(q - p + 1)]

    def k1_i(i):
        return max(-a, -b) <= i - a <= min(n - a - 1, n - b - 1)

    def k1_j(j):
        return max(-a, -b) <= j - b <= min(n - a - 1, n - b - 1)

    def k2_i(i):
        return max(-a, b - n + 1) <= i - a <= min(n - a + 1, b)

    def k2_j(j):
        return max(-a, b - n + 1) <= b - j <= min(n - a + 1, b)

    for i in range(p, q + 1):
        for j in range(r, s + 1):
            if k1_i(i) and k1_j(j) and i - a == j - b:
                grid[i - p][j - r] = "#"

            if k2_i(i) and k2_j(j) and i - a == b - j:
                grid[i - p][j - r] = "#"

    for r in grid:
        print("".join(r))
    return


if __name__ == "__main__":
    main()
