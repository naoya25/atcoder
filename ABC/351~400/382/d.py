import itertools


def main():
    n, m = map(int, input().split())

    sequences = []
    for comb in itertools.combinations(range(1, m - 9 * (n - 1) + 1), n):
        l = list(comb)
        for i in range(n):
            l[i] += 9 * i
        sequences.append(l)
    print(len(sequences))
    for seq in sequences:
        print(*seq)

    return


if __name__ == "__main__":
    main()
