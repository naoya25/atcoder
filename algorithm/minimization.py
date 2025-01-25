# 入力の図形の余白を削除して最小化する
def minimization(grid, h, w):
    sr, er, sc, ec = 0, h, 0, w
    # 上
    for i in range(h):
        if all(e == "." for e in grid[i]):
            sr += 1
        else:
            break
    # 下
    for i in range(h - 1, -1, -1):
        if all(e == "." for e in grid[i]):
            er -= 1
        else:
            break
    # 左
    for i in range(w):
        arr = [r[i] for r in grid]
        if all(e == "." for e in arr):
            sc += 1
        else:
            break
    # 右
    for i in range(w):
        arr = [r[-i - 1] for r in grid]
        if all(e == "." for e in arr):
            ec -= 1
        else:
            break

    return [r[sc:ec] for r in grid[sr:er]], sr, sc, er - sr, ec - sc
