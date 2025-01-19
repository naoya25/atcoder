def main():
    n, d, p = map(int, input().split())
    f = list(map(int, input().split()))
    ans = sum(f)
    f.sort()

    i = 1
    f_sum = sum(f[-d:])
    while f_sum > p:
        ans -= f_sum
        ans += p
        i += 1
        f_sum = sum(f[-i * d : -(i - 1) * d])
    print(ans)

    return


if __name__ == "__main__":
    main()
