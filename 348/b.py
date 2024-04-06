import math


def main():
    n = int(input())
    dots = [tuple(map(int, input().split())) for _ in range(n)]
    for i, p1 in enumerate(dots):
        x1, y1 = p1
        max_distance = 0
        max_point = 0
        for j, p2 in enumerate(dots):
            if i == j:
                continue
            x2, y2 = p2
            d = calc_distance(x1, y1, x2, y2)
            if d > max_distance:
                max_distance = d
                max_point = j + 1
        print(max_point)


def calc_distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx**2 + dy**2)


if __name__ == "__main__":
    main()
