def main():

    h, w, n = map(int, input().split())

    row = [set() for _ in range(h + 1)]
    col = [set() for _ in range(w + 1)]

    for _ in range(n):
        x, y = map(int, input().split())
        row[x].add(y)
        col[y].add(x)

    q = int(input())
    ans = []

    for _ in range(q):
        t, d = map(int, input().split())

        if t == 1:
            ans.append(str(len(row[d])))

            for y in list(row[d]):
                col[y].discard(d)
            row[d].clear()

        else:
            ans.append(str(len(col[d])))

            for x in list(col[d]):
                row[x].discard(d)
            col[d].clear()

    for a in ans:
        print(a)
    return


if __name__ == "__main__":
    main()
