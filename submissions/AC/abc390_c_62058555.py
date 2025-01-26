# URL: https://atcoder.jp/contests/abc390/submissions/62058555
# id: 62058555
# epoch_second: 1737808082
# problem_id: abc390_c
# contest_id: abc390
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 300.0
# length: 1176
# result: AC
# execution_time: 191


# submitted code
def minimization(grid, h, w):
    sr, er, sc, ec = 0, h, 0, w
    # 上
    for i in range(h):
        if all(e == "." or e == "?" for e in grid[i]):
            sr += 1
        else:
            break
    # 下
    for i in range(h - 1, -1, -1):
        if all(e == "." or e == "?" for e in grid[i]):
            er -= 1
        else:
            break
    # 左
    for i in range(w):
        arr = [r[i] for r in grid]
        if all(e == "." or e == "?" for e in arr):
            sc += 1
        else:
            break
    # 右
    for i in range(w):
        arr = [r[-i - 1] for r in grid]
        if all(e == "." or e == "?" for e in arr):
            ec -= 1
        else:
            break

    return [r[sc:ec] for r in grid[sr:er]], sr, sc, er - sr, ec - sc


def main():
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]

    new_grid, sr, sc, er, ec = minimization(grid, h, w)

    all_hash_or_question = all(
        all(cell == "#" or cell == "?" for cell in row) for row in new_grid
    )
    print("Yes" if all_hash_or_question else "No")


if __name__ == "__main__":
    main()
