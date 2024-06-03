def main():

    t = int(input())

    m = 998244353
    for _ in range(t):
        a1, a2, a3 = map(int, input().split())
        diff = a3 - max(a1, a2)
        if not (0 <= diff < 2):
            print(0)
            continue
        min1 = 10 ** (a1 - 1)
        min2 = 10 ** (a2 - 1)
        min3 = 10 ** (a3 - 1)
        max1 = 10**a1 - 1
        max2 = 10**a2 - 1
        max3 = 10**a3 - 1

        lim1 = 0
        if min3 <= min1 + min2 <= max3 and min3 <= min1 + max2 <= max3:
            lim1 = (max2 - min2 + 1) % m
        elif min3 <= min1 + min2 <= max3:
            lim1 = (max3 - (min1 + min2) + 1) % m
        elif min3 <= min1 + max2 <= max3:
            lim1 = (min1 + max2 - min3 + 1) % m

        lim2 = 0
        if min3 <= max1 + min2 <= max3 and min3 <= max1 + max2 <= max3:
            lim2 = (max2 - min2 + 1) % m
        elif min3 <= max1 + min2 <= max3:
            lim2 = (max3 - (max1 + min2) + 1) % m
        elif min3 <= max1 + max2 <= max3:
            lim2 = (max1 + max2 - min3 + 1) % m

        big_lim = max(lim1, lim2)
        small_lim = min(lim1, lim2)
        ans1 = max(0, (big_lim * (big_lim + 1) // 2) % m)
        ans2 = max(0, (small_lim * (small_lim - 1) // 2) % m)
        print(ans1 - ans2)

    return


if __name__ == "__main__":
    main()
