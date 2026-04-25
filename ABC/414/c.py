def main():
    a = int(input())
    n = int(input())

    s_lim = str(n)
    max_len = len(s_lim)

    pal = []

    for length in range(1, max_len + 1):
        half_len = (length + 1) // 2
        start = 10 ** (half_len - 1)  # 左端 0 禁止
        end = 10**half_len

        for left in range(start, end):
            s = str(left)
            p = int(s + (s[::-1] if length % 2 == 0 else s[-2::-1]))
            if p > n:
                break
            pal.append(p)

    if a == 10:
        print(sum(pal))
        return

    ans = 0
    for p in pal:
        p_copy = p
        digits = []
        while p:
            digits.append(p % a)
            p //= a

        if digits == digits[::-1]:
            ans += p_copy
    print(ans)


if __name__ == "__main__":
    main()
