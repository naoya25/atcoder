def main():
    n = int(input())
    base = list(map(str, [0, 2, 4, 6, 8]))
    digits = calc_digits(n)
    ans_str = base[n % 5 - 1]
    if digits == 1:
        print(ans_str)
        return

    for i in range(1, digits):
        ans_str = base[(n - 1) // (5**i) % 5] + ans_str
    print(ans_str)


# 5 ^ k < n
# 答えの桁数を計算
def calc_digits(n):
    k = 0
    num = 1
    while num < n:
        num *= 5
        k += 1

    return k


if __name__ == "__main__":
    main()
