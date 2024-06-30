def main():
    n, k = map(int, input().split())

    expected_value = 1

    # 各操作ごとに期待値がどのように変動するかを計算
    for _ in range(k):
        # 全N個のボールの中から2つを選ぶ方法の数はN*(N-1)
        expected_value = (expected_value * (n - 1) + (n + 1) // 2) % m

    print(expected_value)
    return


if __name__ == "__main__":
    main()


def modinv(a, mod):
    # フェルマーの小定理を用いて逆元を求める
    return pow(a, mod - 2, mod)


def division_mod(p, q):
    m = 998244353
    inv_q = modinv(q, m)
    result = (p * inv_q) % m
    return result


# 例として p = 3, q = 2 とします
p = 3
q = 2

# 計算
result = division_mod(p, q)
result
