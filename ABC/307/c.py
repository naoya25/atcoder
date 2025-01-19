def main():
    ha, wa = map(int, input().split())
    grid_a = [list(input()) for _ in range(ha)]
    hb, wb = map(int, input().split())
    grid_b = [list(input()) for _ in range(hb)]
    hx, wx = map(int, input().split())
    grid_x = [list(input()) for _ in range(hx)]

    a, ha, wa = minimization(grid_a, ha, wa)
    b, hb, wb = minimization(grid_b, hb, wb)
    x, hx, wx = minimization(grid_x, hx, wx)

    # あとで消す-------
    # print("a", ha, wa)
    # for r in a:
    #     print(r)
    # print("b", hb, wb)
    # for r in b:
    #     print(r)
    # print("x", hx, wx)
    # for r in x:
    #     print(r)

    # ここまで---------

    def judge(dxa, dya, dxb, dyb):
        for r in range(hx):
            for c in range(wx):
                if x[r][c] == ".":
                    if 0 <= c - dxa < wa and 0 <= r - dya < ha:
                        if a[r - dya][c - dxa] != ".":
                            return False
                    if 0 <= c - dxb < wb and 0 <= r - dyb < hb:
                        if b[r - dyb][c - dxb] != ".":
                            return False
                else:
                    if 0 <= c - dxa < wa and 0 <= r - dya < ha:
                        if a[r - dya][c - dxa] == "#":
                            continue
                    if 0 <= c - dxb < wb and 0 <= r - dyb < hb:
                        if b[r - dyb][c - dxb] == "#":
                            continue
                    return False
        return True

    for dxa in range(wx - wa + 1):
        for dya in range(hx - ha + 1):
            for dxb in range(wx - wb + 1):
                for dyb in range(hx - hb + 1):
                    if judge(dxa, dya, dxb, dyb):
                        print("Yes")
                        return
    print("No")
    return


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

    return [r[sc:ec] for r in grid[sr:er]], er - sr, ec - sc


if __name__ == "__main__":
    main()
