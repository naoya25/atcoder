def main():
    n, m = map(int, input().split())

    rows_black_max = [-1] * n
    cols_black_max = [-1] * n
    rows_white_min = [n] * n
    cols_white_min = [n] * n

    for _ in range(m):
        x, y, c = input().split()
        x = int(x) - 1
        y = int(y) - 1
        if c == "B":
            for i in range(x + 1):
                rows_black_max[i] = max(rows_black_max[i], y)
            for i in range(y + 1):
                cols_black_max[i] = max(cols_black_max[i], x)
        else:
            for i in range(x, n):
                rows_white_min[i] = min(rows_white_min[i], y)
            for i in range(y, n):
                cols_white_min[i] = min(cols_white_min[i], x)

    for i in range(n):
        if rows_black_max[i] >= rows_white_min[i]:
            print("No")
            break

        if cols_black_max[i] >= cols_white_min[i]:
            print("No")
            break
    else:
        print("Yes")

    return


if __name__ == "__main__":
    main()
