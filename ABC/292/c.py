def count_divisors(x):
    count = 0
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            if i == x // i:
                count += 1
            else:
                count += 2
    return count


def main():
    n = int(input())
    ans = 0

    for i in range(1, n + 1):
        ab = i
        cd = n - i

        sum_ab = count_divisors(ab)
        sum_cd = count_divisors(cd)

        ans += sum_ab * sum_cd

    print(ans)


if __name__ == "__main__":
    main()
