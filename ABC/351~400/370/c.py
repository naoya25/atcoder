def main():
    s = list(input())
    t = list(input())
    if s == t:
        print(0)
        return

    ud = []
    for si, ti in zip(s, t):
        ud.append(ord(si) - ord(ti))
    # print(ud)

    x = []
    for i in range(len(s)):
        if ud[i] <= 0:
            continue
        s[i] = t[i]
        x.append(s.copy())

    for i in range(len(s) - 1, -1, -1):
        if ud[i] >= 0:
            continue
        s[i] = t[i]
        x.append(s.copy())

    print(len(x))
    for r in x:
        print("".join(r))

    return


if __name__ == "__main__":
    main()
