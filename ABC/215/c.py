from itertools import permutations


def main():
    s, k = input().split()
    k = int(k) - 1

    s_arr = set()

    for p in permutations(s):
        s_arr.add("".join(p))
    print(sorted(s_arr)[k])


if __name__ == "__main__":
    main()
