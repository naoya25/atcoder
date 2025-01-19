def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())

    def judge(a, b, c, d):
        r1 = h1 - a - b
        r2 = h2 - c - d
        r3 = w3 - r1 - r2
        c1 = w1 - a - c
        c2 = w2 - b - d
        c3 = h3 - c1 - c2
        return all(i > 0 for i in [r1, r2, r3, c1, c2, c3]) and r3 == c3

    ans = sum(
        judge(a, b, c, d)
        for a in range(1, min(h1, w1))
        for b in range(1, min(h1, w2))
        for c in range(1, min(h2, w1))
        for d in range(1, min(h2, w2))
    )

    print(ans)
    return


if __name__ == "__main__":
    main()
