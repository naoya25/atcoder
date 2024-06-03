def main():
    h, w, n = map(int, input().split())
    rows, cols = set(), set()
    nums = []
    for _ in range(n):
        a, b = map(lambda x: int(x) - 1, input().split())
        nums.append((a, b))
        rows.add(a)
        cols.add(b)

    rows_arr = sorted(list(rows))
    cols_arr = sorted(list(cols))

    for i in range(1, n + 1):
        a, b = nums[i - 1]
        print(rows_arr.index(a) + 1, cols_arr.index(b) + 1)

    return


if __name__ == "__main__":
    main()
