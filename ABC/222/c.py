def main():
    n, m = map(int, input().split())
    a = [input() for _ in range(2 * n)]
    player = {i: 0 for i in range(2 * n)}
    ranking = list(range(2 * n))
    for r in range(m):
        for k in range(n):
            s1 = a[ranking[2 * k]][r]
            s2 = a[ranking[2 * k + 1]][r]
            j = gcp(s1, s2)
            if j == 1:
                player[ranking[2 * k]] += 1
            elif j == -1:
                player[ranking[2 * k + 1]] += 1
        ranking = sorted(player.keys(), key=lambda k: (-player[k], k))

    for r in ranking:
        print(r + 1)

    return


def gcp(s1, s2):
    # draw
    if (s1 == "G" and s2 == "G") or (s1 == "C" and s2 == "C") or (s1 == "P" and s2 == "P"):
        return 0

    # s1 win
    if (s1 == "G" and s2 == "C") or (s1 == "C" and s2 == "P") or (s1 == "P" and s2 == "G"):
        return 1

    return -1


if __name__ == "__main__":
    main()

