def main():
    n, m = map(int, input().split())
    s = [list(input()) for _ in range(n)]
    t = [list(input()) for _ in range(m)]

    def judge(i, j):
        for k in range(m):
            for l in range(m):
                if s[i + k][j + l] != t[k][l]:
                    return False
        return True

    for i in range(n - m + 1):
        for j in range(n - m + 1):

            if judge(i, j):
                print(i + 1, j + 1)
                return
    return


if __name__ == "__main__":
    main()
