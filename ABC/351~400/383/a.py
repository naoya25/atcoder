def main():
    n = int(input())
    cw = 0
    ct = 1
    for _ in range(n):
        t, v = map(int, input().split())
        cw -= min(t - ct, cw)
        ct = t
        cw += v
    print(cw)

    return


if __name__ == "__main__":
    main()
