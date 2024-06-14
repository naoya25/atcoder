def main():
    h, w, n = map(int, input().split())
    rows, cols = set(), set()
    nums = []
    for _ in range(n):
        a, b = map(lambda x: int(x) - 1, input().split())
        nums.append((a, b))
        rows.add(a)
        cols.add(b)

    rows = sorted(rows)
    cols = sorted(cols)
    rows_dict = {rows[i]: i + 1 for i in range(len(rows))}
    cols_dict = {cols[i]: i + 1 for i in range(len(cols))}
    # print(rows_dict)

    for i in range(n):
        a, b = nums[i]
        print(rows_dict[a], cols_dict[b])


if __name__ == "__main__":
    main()
