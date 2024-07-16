from collections import defaultdict


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a_dict = defaultdict(list)

    for i in range(n):
        a_dict[a[i]].append(i)

    for _ in range(q):
        x, k = map(int, input().split())
        if len(a_dict[x]) < k:
            print(-1)
        else:
            print(a_dict[x][k - 1] + 1)

    return


if __name__ == "__main__":
    main()
