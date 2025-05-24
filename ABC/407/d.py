"""
XOR: 1が奇数個あるときのみ1
とりまBFSで解く
1列ごとに探索して、その列終わったら1個次の行に進む
普通に2重ループでもいけるかも
"""


def main():
    h, w = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(h)]
    max_score = 0

    def get_score(used):
        xor_sum = 0
        for i in range(h):
            for j in range(w):
                if not used[i][j]:
                    xor_sum ^= grid[i][j]
        return xor_sum

    stack = []  # (i, j, used 状態)
    initial_used = [[False] * w for _ in range(h)]
    stack.append((0, 0, initial_used))

    while stack:
        i, j, used = stack.pop()

        if i == h:
            max_score = max(max_score, get_score(used))
            continue
        if j == w:
            stack.append((i + 1, 0, [row[:] for row in used]))
            continue
        if used[i][j]:
            stack.append((i, j + 1, [row[:] for row in used]))
            continue

        # 使わない場合
        stack.append((i, j + 1, [row[:] for row in used]))

        # 横ペアを使う場合
        if j + 1 < w and not used[i][j + 1]:
            new_used = [row[:] for row in used]
            new_used[i][j] = new_used[i][j + 1] = True
            stack.append((i, j + 2, new_used))

        # 縦ペアを使う場合
        if i + 1 < h and not used[i + 1][j]:
            new_used = [row[:] for row in used]
            new_used[i][j] = new_used[i + 1][j] = True
            stack.append((i, j + 1, new_used))

    print(max_score)


if __name__ == "__main__":
    main()
