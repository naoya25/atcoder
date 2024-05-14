def main():
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    n = int(input())
    # 薬の場所を0から始まる座標系として辞書型に保存
    drug_spot = {}
    for _ in range(n):
        r, c, e = map(int, input().split())
        drug_spot[(r - 1, c - 1)] = e

    # スタートとゴール位置取得
    for r in range(h):
        for c in range(w):
            if grid[r][c] == "S":
                sr, sc = r, c
                grid[r][c] = "."
            if grid[r][c] == "T":
                tr, tc = r, c
                grid[r][c] = "."
    # print(grid)
    # print(drug_spot)  # ex. {(0, 0): 3, (0, 2): 5, (2, 1): 1, (1, 2): 1}

    # 初期位置が薬の場所じゃなかったら終わり
    if (sr, sc) not in drug_spot.keys():
        print("No")
        return

    visited = [[False] * (w) for _ in range(h)]
    stack = [(sr, sc, 0)]  # 初期位置の座標r,c, 初期エネルギー
    visited[sr][sc] = True
    while stack:
        print(stack)
        r, c, energy = stack.pop()

        if energy < 0:  # エネルギー切れ
            continue
        if (r, c) == (tr, tc):  # ゴール
            print("Yes")
            return
        if (r, c) in drug_spot.keys():  # エネルギーチャージ
            energy = max(drug_spot[(r, c)], energy)
            print((r, c), drug_spot[(r, c)], energy)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] == ".":
                visited[nr][nc] = True
                stack.append((nr, nc, energy - 1))

    print("No")
    return


if __name__ == "__main__":
    main()
