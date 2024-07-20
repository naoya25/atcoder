from collections import defaultdict


def main():
    n, q = map(int, input().split())

    dd = defaultdict(set)
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            dd[a].add(b)
        elif t == 2:
            if b in dd[a]:
                dd[a].remove(b)
        else:
            if b in dd[a] and a in dd[b]:
                print("Yes")
            else:
                print("No")

    return


if __name__ == "__main__":
    main()
