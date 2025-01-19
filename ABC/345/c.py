import string


def main():
    s = input()
    s_count = {a: s.count(a) for a in string.ascii_lowercase if a in s}
    num = 0
    for k, v in s_count.items():
        if v < 2:
            continue
        num += comb(v)

    print(comb(len(s)) if num == 0 else comb(len(s)) - num + 1)


def comb(n):  # nC2
    return n * (n - 1) // 2


if __name__ == "__main__":
    main()
