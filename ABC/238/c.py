def main():
    n = int(input())
    m = 998244353
    l = len(str(n))
    # print(l)
    ans = 0
    for i in range(l - 1):
        num = 9 * 10**i
        ans += num * (num + 1) // 2

    num = n - 10 ** (l - 1) + 1
    ans += num * (num + 1) // 2
    print(ans % m)
    return


if __name__ == "__main__":
    main()
