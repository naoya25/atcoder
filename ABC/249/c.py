from collections import defaultdict


def main():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0

    for m in range(1, 1 << n):
        dd = defaultdict(int)
        for i in range(n):
            if m >> i & 1:
                for si in s[i]:
                    dd[si] += 1

        cnt = 0
        for _, v in dd.items():
            if v == k:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
    return


if __name__ == "__main__":
    main()
