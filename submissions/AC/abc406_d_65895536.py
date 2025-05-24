# URL: https://atcoder.jp/contests/abc406/submissions/65895536
# id: 65895536
# epoch_second: 1747485874
# problem_id: abc406_d
# contest_id: abc406
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 400.0
# length: 780
# result: AC
# execution_time: 728


# submitted code
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
