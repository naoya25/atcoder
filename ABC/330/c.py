def main():
    d = int(input())
    a = int(d ** (1 / 2))
    ans = (a + 1) ** 2 - d  # x^2 > d の最初のxを試す
    for x in range(a + 1):  # xを全パターン(x^2 <= d)
        y = int((d - x**2) ** (1 / 2))
        u_ans = d - (x**2 + y**2)
        o_ans = x**2 + (y + 1) ** 2 - d
        ans = min(u_ans, o_ans, ans)
    print(ans)
    return


if __name__ == "__main__":
    main()
