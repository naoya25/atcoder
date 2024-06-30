def main():
    n, a = map(int, input().split())
    t = list(map(int, input().split()))

    t[0] += a
    for i in range(1, n):
        if t[i] <= t[i - 1]:
            t[i] = t[i - 1] + a
        else:
            t[i] += a
    for ti in t:
        print(ti)
    return


if __name__ == "__main__":
    main()
