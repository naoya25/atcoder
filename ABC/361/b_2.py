def main():
    a, b, c, d, e, f = map(int, input().split())
    g, h, i, j, k, l = map(int, input().split())

    def judge(x, y, z):
        if a < x < d and b < y < e and c < z < f:
            return True
        return False

    if (
        judge(g, h, i)
        or judge(g, h, l)
        or judge(g, k, i)
        or judge(j, h, i)
        or judge(g, k, l)
        or judge(j, h, l)
        or judge(j, k, i)
        or judge(j, k, l)
    ):
        print("Yes")
        return
    print("No")
    return


if __name__ == "__main__":
    main()
