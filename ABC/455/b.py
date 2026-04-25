def main():
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]

    ans = 0
    for h1 in range(h):
        for h2 in range(h1, h):
            for w1 in range(w):
                for w2 in range(w1, w):
                    ans = ans + judge(grid, h1, h2, w1, w2)

    print(ans)
    return


def judge(grid, h1, h2, w1, w2):
    for i in range(h1, h2 + 1):
        for j in range(w1, w2 + 1):
            if grid[i][j] != grid[h1 + h2 - i][w1 + w2 - j]:
                return 0

    return 1


if __name__ == "__main__":
    main()
