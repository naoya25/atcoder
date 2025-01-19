def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))

    if j(a, b, c) or j(b, c, d) or j(c, d, a) or j(d, a, b):
        print("No")
    else:
        print("Yes")
    return


def j(a, b, c):
    ax, ay = a
    bx, by = b
    cx, cy = c

    b1x = ax - bx
    b1y = ay - by
    b2x = cx - bx
    b2y = cy - by

    return b1x * b2y - b1y * b2x > 0


if __name__ == "__main__":
    main()
