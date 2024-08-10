# def main():
#     n, d = map(int, input().split())
#     dots = []

#     for _ in range(n):
#         x, y = map(int, input().split())
#         dots.append((x, y))

#     x_sorted = sorted(x for x, y in dots)
#     y_sorted = sorted(y for x, y in dots)

#     def calc_dist(x, y):  # 2*10**5
#         x_dist = sum(abs(x - xi) for xi in x_sorted)
#         y_dist = sum(abs(y - yi) for yi in y_sorted)
#         return x_dist + y_dist

#     x_min, x_max = x_sorted[0], x_sorted[-1]
#     y_min, y_max = y_sorted[0], y_sorted[-1]

#     count = 0
#     for x in range(x_min - d, x_max + d + 1):
#         for y in range(y_min - d, y_max + d + 1):
#             if calc_dist(x, y) <= d:
#                 count += 1

#     print(count)


# if __name__ == "__main__":
#     main()

"""
距離がdの一番遠い点を全て調べることができたら
同一直線(yが同じ)の点はそのxの最大値、最小値がわかれば間は計算する必要なし？？

2分探索感あるかもな
2次元ではなく、1じげんの数直線上に全ての点があるとしたら？？

1次元だったとしたら
xしか見てないけど、これにyのabsのsumしたやつ分狭めれば範囲もとまりそう
yの値がわかれば、10**5くらいで個数が求まる
最初のy固定してxの個数求めたら、あとはピラミッド状に増えるだけか

方針
xとyのそれぞれ中央値取得
xを中央値で固定した時のyの最大値と最小値求める
yを固定でも同じようにする
十字架みたいな形になって、その菱形の面積を求める
時間足らんwwwww
"""


def main():
    n, d = map(int, input().split())
    dots = []

    for _ in range(n):
        x, y = map(int, input().split())
        dots.append((x, y))

    x_sorted = sorted(x for x, y in dots)
    y_sorted = sorted(y for x, y in dots)

    def calc_dist(x, y):  # 2*10**5
        x_dist = sum(abs(x - xi) for xi in x_sorted)
        y_dist = sum(abs(y - yi) for yi in y_sorted)
        return x_dist + y_dist

    x_median = x_sorted[n // 2]
    y_median = y_sorted[n // 2]

    x_min, x_max = x_sorted[0], x_sorted[-1]
    y_min, y_max = y_sorted[0], y_sorted[-1]

    count = 0
    for x in range(x_min - d, x_max + d + 1):
        for y in range(y_min - d, y_max + d + 1):
            if calc_dist(x, y) <= d:
                count += 1

    print(count)


if __name__ == "__main__":
    main()

