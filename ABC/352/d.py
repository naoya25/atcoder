from itertools import combinations


def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    combs = combinations(range(n), k)

    ans = float("inf")

    for comb in combs:
        p_temp = list(map(lambda i: p[i], comb))
        if max(p_temp) - min(p_temp) == len(p_temp) - 1:
            ans = min(ans, len(p_temp) - 1)
    print(ans)


if __name__ == "__main__":
    main()
