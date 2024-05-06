def main():
    n = int(input())
    a, b = calc_pow(n)
    ans = (n - b) * a + (a + 2) * b
    print(ans)


# n = 2**a + b
def calc_pow(n):
    a = 0
    b = 0
    num = 1
    while num < n:  # n →10^17
        num *= 2
        a += 1
    a -= 1
    num //= 2
    b = n - num

    return a, b


if __name__ == "__main__":
    main()
