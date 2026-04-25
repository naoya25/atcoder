from itertools import combinations


def main():
    n = int(input())
    s = [input() for _ in range(n)]

    s_set = set()
    for pair in combinations(s, 2):
        s_set.add(pair[0] + pair[1])
        s_set.add(pair[1] + pair[0])

    print(len(s_set))

    return


if __name__ == "__main__":
    main()
