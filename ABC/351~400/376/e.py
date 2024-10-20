from itertools import combinations


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        ans = calc_ans(n, k, a, b)
        print(ans)

    return


def calc_ans(n, k, a, b):
    min_ans = float("inf")
    for indices in combinations(range(n), k):
        max_a = max(a[i] for i in indices)
        sum_b = sum(b[i] for i in indices)

        min_ans = min(max_a * sum_b, min_ans)
    return min_ans


if __name__ == "__main__":
    main()
