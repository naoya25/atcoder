import itertools


def main():
    c = "".join(["".join(input().split()) for _ in range(3)])
    m = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2  # 9!

    # まず、同じ列、行、斜めに同じ数字のペアがゾン祭するかチェック
    # 存在していれば、そのペアが先に見られたかチェックする

    i_arr = (
        [[0, 1, 2], [3, 4, 5], [6, 7, 8]]  # よこ
        + [[0, 3, 6], [1, 4, 7], [2, 5, 8]]  # たて
        + [[0, 4, 8], [2, 4, 6]]  # 斜め
    )

    judge_i_arr = []  # 同じ数字のペアが存在する3つ
    for a in i_arr:
        if len(set(map(lambda x: c[x], a))) < 3:
            judge_i_arr.append(a)
    # print(judge_i_arr)

    cnt = 0
    for p in itertools.permutations(range(9)):  # 見る順番の全パターン
        if not judge(c, p, judge_i_arr):
            cnt += 1
    print(cnt / m)
    return


def judge(c, p, judge_i_arr):  # がっかりしたらtrue
    for ia, ib, ic in judge_i_arr:
        if c[ia] == c[ib] and p[ic] > max(p[ia], p[ib]):
            return True
        elif c[ib] == c[ic] and p[ia] > max(p[ib], p[ic]):
            return True
        elif c[ic] == c[ia] and p[ib] > max(p[ic], p[ia]):
            return True
    return False


if __name__ == "__main__":
    main()
