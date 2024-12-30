def main():
    k = int(input())
    s = input()
    t = input()

    ls, lt = len(s), len(t)

    if ls + 1 == lt:
        if judge1(s, t):
            print("Yes")
        else:
            print("No")
        return
    elif ls - 1 == lt:
        if judge2(s, t):
            print("Yes")
        else:
            print("No")
        return
    elif ls == lt:
        if judge3(s, t):
            print("Yes")
        else:
            print("No")
    else:
        print("No")


def judge1(s, t):
    i = 0
    j = 0
    cnt = 0
    while i < len(s) and j < len(t):
        if s[i] != t[j]:
            cnt += 1
            j += 1
        i += 1
        j += 1
    return cnt <= 1


def judge2(s, t):
    i = 0
    j = 0
    cnt = 0
    while i < len(s) and j < len(t):
        if s[i] != t[j]:
            cnt += 1
            i += 1
        i += 1
        j += 1
    return cnt <= 1


def judge3(s, t):
    cnt = 0
    for si, ti in zip(s, t):
        if si != ti:
            cnt += 1
    return cnt <= 1


if __name__ == "__main__":
    main()
