def main():
    n, m = map(int, input().split())
    points = [0] * n
    s = [input() for _ in range(n)]

    for i in range(m):
        x, y = [], []

        for j in range(n):
            if s[j][i] == "0":
                x.append(j)
            else:
                y.append(j)
        if len(x) == 0 or len(y) == 0:
            for j in range(n):
                points[j] += 1
        elif len(x) < len(y):
            for j in x:
                points[j] += 1
        else:
            for j in y:
                points[j] += 1

    max_point = max(points)
    ans = []
    for i in range(n):
        if points[i] == max_point:
            ans.append(i + 1)
    print(*ans)

    return


if __name__ == "__main__":
    main()
