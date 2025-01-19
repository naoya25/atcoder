from itertools import product


def main():
    n, k = map(int, input().split())
    r = list(map(int, input().split()))
    [2, 1, 3]
    [[1, 2], [1], [1, 2, 3]]

    for a in list(product(*[range(1, ri + 1) for ri in r])):
        if sum(a) % k == 0:
            print(*a)
    return


if __name__ == "__main__":
    main()
