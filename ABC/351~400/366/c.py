from collections import defaultdict


def main():
    q = int(input())

    dd = defaultdict(int)
    cnt = 0
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            if dd[query[1]] == 0:
                cnt += 1
            dd[query[1]] += 1
        elif query[0] == 2:
            if dd[query[1]] == 1:
                cnt -= 1
            dd[query[1]] -= 1
        else:
            print(cnt)

    return


if __name__ == "__main__":
    main()
