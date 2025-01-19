from collections import defaultdict


def main():
    n = int(input())
    s = list(map(int, list(input())))
    w = list(map(int, input().split()))
    p = defaultdict(lambda: [0, 0])  # 子供の数、大人の数
    for si, wi in zip(s, w):
        if si == 1:
            p[wi][1] += 1
        else:
            p[wi][0] += 1
    k = sorted(p.keys())

    ans = max(sum(s), n - sum(s))
    cnt = sum(s)
    for i in k:
        cnt += p[i][0] - p[i][1]
        ans = max(ans, cnt)
    print(ans)
    return


if __name__ == "__main__":
    main()
