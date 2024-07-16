
def main():
    n, t = map(int, input().split())
    a = list(map(lambda x: int(x) - 1, input().split()))

    # 各行と各列のカウント
    row_counts = [0] * n
    col_counts = [0] * n
    diag1_count = 0
    diag2_count = 0

    for i in range(t):
        index = a[i]
        row = index // n
        col = index % n

        row_counts[row] += 1
        col_counts[col] += 1

        if row == col:
            diag1_count += 1

        if row + col == n - 1:
            diag2_count += 1

        # チェック
        if row_counts[row] == n or col_counts[col] == n or diag1_count == n or diag2_count == n:
            print(i + 1)
            return

    print(-1)
    return


if __name__ == "__main__":
    main()
