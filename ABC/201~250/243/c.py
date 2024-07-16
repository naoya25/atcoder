from collections import defaultdict


def main():
    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    s = input()

    dd = defaultdict(list)
    for i, j in zip(xy, s):
        x, y = i
        dd[y].append((x, j))

    for k in dd.keys():
        v = dd[k]
        if len(v) < 2:
            continue
        v.sort(key=lambda x: x[0])
        j = False
        for xd in v:
            if xd[1] == "R":
                j = True
            if j and xd[1] == "L":
                print("Yes")
                return
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
