def main():
    n = int(input())
    ms = 0
    mf = 0
    mi = 0
    fs = []
    for i in range(n):
        f, s = map(int, input().split())
        fs.append([f, s])
        if s > ms:
            ms = s
            mf = f
            mi = i
    # print(ms, mf, mi)

    ns = 0
    for i in range(n):
        if i == mi:
            continue
        f, s = fs[i]
        if f == mf:
            ns = max(ns, s // 2)
        else:
            ns = max(ns, s)
    print(ms + ns)

    return


if __name__ == "__main__":
    main()
