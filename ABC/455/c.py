def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))

    a_dict = {}
    for a in a_list:
        a_dict[a] = a_dict.get(a, 0) + 1

    a_mul = [k * v for k, v in a_dict.items()]
    a_mul.sort(reverse=True)

    print(sum(a_mul[k:]))

    return


if __name__ == "__main__":
    main()
