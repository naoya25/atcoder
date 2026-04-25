def main():
    n = int(input())
    sl = []
    m = 0
    ml = []
    for _ in range(n):
        s = input()
        sl.append(s)
        ml.append(len(s))
        m = max(m, len(s))

    for i, s in enumerate(sl):
        k = (m - ml[i]) // 2
        print("." * k + s + "." * k)

    return


if __name__ == "__main__":
    main()
