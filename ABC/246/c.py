def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = sum([ai // x for ai in a])
    c = [ai % x for ai in a]
    c.sort()
    # print(b)
    # print(c)

    if b >= k:
        print(sum(a) - k * x)
    else:
        if k - b >= n:
            print(0)
            return
        ans = sum(a) - k * x
        for i in range(1, k - b + 1):
            ans += x - c[-i]
        print(ans)

    return


if __name__ == "__main__":
    main()
