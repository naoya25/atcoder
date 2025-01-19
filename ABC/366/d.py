def main():
    n = int(input())
    grid = []
    for _ in range(n):
        r = [list(map(int, input().split())) for _ in range(n)]
        grid.append(r)

    # 累積和
    cumsum = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                cumsum[i][j][k] = (
                    grid[i - 1][j - 1][k - 1]
                    + cumsum[i - 1][j][k]
                    + cumsum[i][j - 1][k]
                    + cumsum[i][j][k - 1]
                    - cumsum[i - 1][j - 1][k]
                    - cumsum[i - 1][j][k - 1]
                    - cumsum[i][j - 1][k - 1]
                    + cumsum[i - 1][j - 1][k - 1]
                )

    q = int(input())
    for _ in range(q):
        l1, r1, l2, r2, l3, r3 = map(lambda x: int(x) - 1, input().split())

        ans = (
            cumsum[r1 + 1][r2 + 1][r3 + 1]
            - cumsum[l1][r2 + 1][r3 + 1]
            - cumsum[r1 + 1][l2][r3 + 1]
            - cumsum[r1 + 1][r2 + 1][l3]
            + cumsum[l1][l2][r3 + 1]
            + cumsum[l1][r2 + 1][l3]
            + cumsum[r1 + 1][l2][l3]
            - cumsum[l1][l2][l3]
        )
        print(ans)

    return


if __name__ == "__main__":
    main()
