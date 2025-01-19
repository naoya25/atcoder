from itertools import combinations


def main():
    n, m = map(int, input().split())
    s = []
    ans = set([i + 1 for i in range(n)])

    for _ in range(m):
        c = int(input())
        si = set(map(int, input().split()))
        s.append(si)

    cnt = 0
    for i in range(1, m + 1):
        c = combinations([j for j in range(m)], i)
        for ci in c:
            tmp = set()
            for k in ci:
                tmp = tmp.union(s[k])
            if ans == tmp:
                cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
