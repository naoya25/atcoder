def main():
    a, b, c, d, e, f = map(int, input().split())
    n = int(input())
    x = list(map(int, input().split()))

    if a + 5 * b + 10 * c + 50 * d + 100 * e + 500 * f < sum(x):
        print("No")
        return

    for xi in x:
        fr = xi // 500
        fp = min(f, fr)
        xi -= 500 * fp
        f -= fp

        er = xi // 100
        ep = min(e, er)
        xi -= 100 * ep
        e -= ep

        dr = xi // 50
        dp = min(d, dr)
        xi -= 50 * dp
        d -= dp

        cr = xi // 10
        cp = min(c, cr)
        xi -= 10 * cp
        c -= cp

        br = xi // 5
        bp = min(b, br)
        xi -= 5 * bp
        b -= bp

        ap = min(a, xi)
        a -= ap
        if ap != xi:
            print("No")
            return

    print("Yes")
    return


if __name__ == "__main__":
    main()


# def main():
#     a, b, c, d, e, f = map(int, input().split())
#     n = int(input())
#     x = list(map(int, input().split()))

#     if a + 5 * b + 10 * c + 50 * d + 100 * e + 500 * f < sum(x):
#         print("No")
#         return

#     coins = [(500, f), (100, e), (50, d), (10, c), (5, b), (1, a)]

#     for xi in x:
#         for value, count in coins:
#             needed = xi // value
#             used = min(count, needed)
#             xi -= value * used
#             coins = [(v, c if v != value else c - used) for v, c in coins]

#         if xi > 0:
#             print("No")
#             return

#     print("Yes")

# if __name__ == "__main__":
#     main()
