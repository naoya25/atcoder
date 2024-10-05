import math
import itertools


def main():
    n, s, t = map(int, input().split())
    abcd = [tuple(map(int, input().split())) for _ in range(n)]

    ans = float("inf")

    for perm in itertools.permutations(abcd):
        for bit in range(1 << n):
            xy = (0, 0)
            total = 0
            for i in range(n):
                a = perm[i][0]
                b = perm[i][1]
                c = perm[i][2]
                d = perm[i][3]
                total += math.sqrt((a - c) ** 2 + (b - d) ** 2) / t
                if bit & (1 << i):  # a,bを先に選ぶ
                    l = math.sqrt((xy[0] - a) ** 2 + (xy[1] - b) ** 2)
                    total += l / s
                    xy = (c, d)
                else:  # c,dを先に選ぶ
                    l = math.sqrt((xy[0] - c) ** 2 + (xy[1] - d) ** 2)
                    total += l / s
                    xy = (a, b)

            ans = min(total, ans)
    # 結果を出力
    print(ans)


if __name__ == "__main__":
    main()
