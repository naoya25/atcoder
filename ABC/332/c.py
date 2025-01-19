def main():
    n, m = map(int, input().split())
    s = input()
    non_t = m  # 綺麗なTシャツの枚数
    logo_t = 0
    ans = 0
    for si in s:
        if si == "0":
            non_t = m
            logo_t = ans
        elif si == "1":
            if non_t > 0:
                non_t -= 1
            elif logo_t > 0:
                logo_t -= 1
            else:
                ans += 1
        else:
            if logo_t > 0:
                logo_t -= 1
            else:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
