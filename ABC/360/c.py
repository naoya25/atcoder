def main():
    n = int(input())
    a = list(map(lambda x: int(x) - 1, input().split()))
    w = list(map(int, input().split()))

    max_baggages = [0] * n
    for i in range(n):
        max_baggages[a[i]] = max(max_baggages[a[i]], w[i])

    print(sum(w) - sum(max_baggages))

    return


if __name__ == "__main__":
    main()
