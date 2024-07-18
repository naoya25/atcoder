def main():
    s = input()
    t = input()
    sd = d(s)
    td = d(t)

    if len(sd) != len(td):
        print("No")
        return

    for si, ti in zip(sd, td):
        ss, sl = si
        ts, tl = ti

        if ss != ts:
            print("No")
            return
        if sl != tl and not (2 <= sl <= tl):
            print("No")
            return

    print("Yes")
    return


def d(s):
    rs = []
    l = 1
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            l += 1
        else:
            rs.append((s[i - 1], l))
            l = 1
    rs.append((s[-1], l))
    return rs


if __name__ == "__main__":
    main()
