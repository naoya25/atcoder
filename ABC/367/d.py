def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a_sum = [0] * (n + 1)
    for i in range(n):
        a_sum[i + 1] = a[i] + a_sum[i]
    print(a_sum)
    return


if __name__ == "__main__":
    main()
