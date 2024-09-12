def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    r, c = [0] * h, [0] * w

    for i in range(h):
        for j in range(w):
            r[i] += a[i][j]
            c[j] += a[i][j]

    for i in range(h):
        for j in range(w):
            print(r[i] + c[j] - a[i][j], end=" ")
        print()

    return


if __name__ == "__main__":
    main()
