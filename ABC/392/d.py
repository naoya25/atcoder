from itertools import combinations
from collections import defaultdict


def main():
    n = int(input())
    tmp_dices = []
    for _ in range(n):
        ka_in = list(map(int, input().split()))
        tmp_dices.append((ka_in[0], ka_in[1:]))

    dices = []
    for dice in tmp_dices:
        k, a = dice
        a_dict = defaultdict(int)
        a_set = set(a)
        for value in a:
            a_dict[value] += 1
        dices.append((k, a_dict, a_set))

    max_p = 0.0
    for (k1, a1, a1_set), (k2, a2, a2_set) in combinations(dices, 2):
        p = 0.0
        for face in a1_set:
            if face in a2_set:
                p += (a1[face] / k1) * (a2[face] / k2)
        max_p = max(max_p, p)
    print(max_p)

    return


if __name__ == "__main__":
    main()
