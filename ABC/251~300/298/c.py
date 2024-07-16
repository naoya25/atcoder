from collections import defaultdict


def main():
    n = int(input())
    q = int(input())

    box = defaultdict(list)
    num = defaultdict(set)
    for _ in range(q):
        qi = list(map(int, input().split()))
        if qi[0] == 1:
            box[qi[2]].append(qi[1])
            num[qi[1]].add(qi[2])
        elif qi[0] == 2:
            r = sorted(box[qi[1]])
            print(*r)
        else:
            r = sorted(num[qi[1]])
            print(*r)

    return


if __name__ == "__main__":
    main()
