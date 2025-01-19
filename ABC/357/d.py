# base ** exp をmodで割ったあまりを計算
def mod_pow(base, exp, mod):
    result = 1
    while exp:
        if exp % 2:
            result = result * base % mod
        base = base * base % mod
        exp //= 2
    return result


def main():
    n_str = input()
    n = int(n_str)
    m = 998244353
    l = len(n_str)

    if n == 1:
        print(1)
        return

    pow_10_l = mod_pow(10, l, m)
    sum_geom = (mod_pow(pow_10_l, n, m) - 1) * mod_pow(pow_10_l - 1, m - 2, m) % m
    result = n % m * sum_geom % m

    print(result)


if __name__ == "__main__":
    main()
