def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    sa = sum(a)
    t %= sa
    for i in range(n):
        t -= a[i]
        if t < 0:
            print(i + 1, a[i] + t)
            return
    return


if __name__ == "__main__":
    main()
