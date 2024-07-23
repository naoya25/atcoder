# wa
def main():
    n = int(input())

    if n <= 10:
        print(n - 1)
        return

    k, i = calc_ki(n)
    ans = find_ans(k, i)
    print(ans)


def find_ans(k, i):
    if k % 2 == 0:
        s = str(10 ** (k // 2 - 1) + i - 1)
        return s + s[::-1]
    else:
        s = str(10 ** (k // 2) + i - 1)
        return s + s[:-1][::-1]


# 桁数kとその中での何番目iか計算
def calc_ki(n):
    arr = [0, 10]  # 0桁と1桁の数値パターン数
    k = 1  # 桁数
    sum_p = 10

    while n > sum_p:
        k += 1
        new_pattern = count_patterns0(k) - count_patterns0(k - 2)
        arr.append(new_pattern)
        sum_p += count_patterns0(k)

    i = n - sum(arr[:k])
    return k, i


# k桁のパターン数(先頭0でも良いとした時)
def count_patterns0(k):
    return 10 ** ((k + 1) // 2)


if __name__ == "__main__":
    main()
