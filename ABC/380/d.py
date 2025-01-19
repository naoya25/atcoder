def main():
    s = input()
    q = int(input())
    k_list = list(map(lambda x: int(x) - 1, input().split()))

    t = s.swapcase()

    results = []
    for k in k_list:
        current_k = k % len(s)

        if (k // len(s)).bit_count() % 2 == 1:
            results.append(t[current_k])
        else:
            results.append(s[current_k])

    print(*results)


if __name__ == "__main__":
    main()
