def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_sum = sum(a)
    a.sort()

    b = [a_sum // n] * n
    for i in range(1, a_sum % n + 1):
        b[-i] += 1
    # print(b)
    ans = 0
    for i in range(n):
        ans += abs(a[i] - b[i])
    print(ans // 2)

    return


if __name__ == "__main__":
    main()
