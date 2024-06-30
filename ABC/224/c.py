from itertools import combinations


def main():
    n = int(input())
    dots = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for d1, d2, d3 in combinations(dots, 3):
        if isTriangle(d1, d2, d3):
            ans += 1
    print(ans)
    return


def isTriangle(d1, d2, d3):
    x1, y1 = d1
    x2, y2 = d2
    x3, y3 = d3
    # 三角形の面積
    # abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0
    a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    return a != 0


if __name__ == "__main__":
    main()
