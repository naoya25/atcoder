def main():
    n, _ = map(int, input().split())
    a_list = list(map(int, input().split()))

    lst = list(range(1, n + 1)) + [a for a in range(1, n + 1) if a not in a_list]
    lst.sort()
    print(lst)

    if len(lst) % 2 == 1:
        lst.append(lst[-1])

    min_sum = sum([lst[i + 1] - lst[i] for i in range(0, len(lst), 2)])

    print(min_sum)


if __name__ == "__main__":
    main()
