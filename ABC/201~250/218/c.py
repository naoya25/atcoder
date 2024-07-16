def main():
    n = int(input())
    s = [list(input()) for _ in range(n)]
    t = [list(input()) for _ in range(n)]
    """memo
    図形最小化
    →h,wが一致してるか判定
    →図形が一致してるか判定
    →4方向回転確かめる
    """

    s = minimization(s, n)
    t = minimization(t, n)
    sh, sw, th, tw = len(s), len(s[0]), len(t), len(t[0])

    # 行数も列数も一致してなかったらNo
    if not (sh == th and sw == tw) and not (sh == tw and sw == th):
        print("No")
        return

    for _ in range(4):
        if is_same(s, t):
            print("Yes")
            return
        t = rot(t)
    print("No")


def rot(grid):
    return [list(row) for row in zip(*grid[::-1])]


def is_same(a, b):
    h, w = len(a), len(a[0])
    if len(b) != h or len(b[0]) != w:
        return False
    for r in range(h):
        for c in range(w):
            if a[r][c] != b[r][c]:
                return False
    return True


def minimization(grid, n):
    sr, er, sc, ec = 0, n, 0, n
    # 上
    for i in range(n):
        if all(e == "." for e in grid[i]):
            sr += 1
        else:
            break
    # 下
    for i in range(n - 1, -1, -1):
        if all(e == "." for e in grid[i]):
            er -= 1
        else:
            break
    # 左
    for i in range(n):
        arr = [r[i] for r in grid]
        if all(e == "." for e in arr):
            sc += 1
        else:
            break
    # 右
    for i in range(n):
        arr = [r[-i - 1] for r in grid]
        if all(e == "." for e in arr):
            ec -= 1
        else:
            break

    retval = []
    for r in grid[sr:er]:
        retval.append(r[sc:ec])
    return retval


if __name__ == "__main__":
    main()
