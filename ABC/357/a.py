def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    if m >= sum(h):
        print(n)
        return
    for i in range(n):
        if m < h[i]:
            print(i)
            return
        m -= h[i]

    return


if __name__ == "__main__":
    main()
