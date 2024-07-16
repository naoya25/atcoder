def main():
    n, k = map(int, input().split())

    k_sum = k * (k + 1) // 2  # 1からkまでの整数の和
    a_set = set(list(map(int, input().split())))
    a_set = {x for x in a_set if x <= k}

    print(k_sum - sum(a_set))


if __name__ == "__main__":
    main()
