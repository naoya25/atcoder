from collections import defaultdict


def main():
    s = input()
    t = input()
    a = list("atcoder@")

    dd = defaultdict(int)
    for ti in t:
        dd[ti] += 1

    at_cnt = 0
    for si in s:
        if si == "@":
            at_cnt += 1
            continue

        if dd[si] > 0:
            dd[si] -= 1
        elif si in a and dd["@"] > 0:
            dd["@"] -= 1
        else:
            print("No")
            return

    if at_cnt <= sum([dd[i] for i in a]):
        print("Yes")
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
