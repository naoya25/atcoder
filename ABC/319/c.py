import itertools


def main():
    c = "".join(["".join(input().split()) for _ in range(3)])
    m = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2  # 9!

    cnt = 0
    for p in itertools.permutations(c):
        if not judge(c, p):
            cnt += 1
    print((m - cnt) / m)
    return


def judge(c, p):
    # よこ
    for i in range(3):
        sc = c[3 * i : 3 * (i + 1)]
        if sc[0] == sc[1]:
            if p[3 * i + 2] > max(p[3 * i], p[3 * i + 1]):
                return False
        if sc[1] == sc[2]:
            if p[3 * i] > max(p[3 * i + 1], p[3 * i + 2]):
                return False
        if sc[2] == sc[0]:
            if p[3 * i + 1] > max(p[3 * i + 2], p[3 * i]):
                return False
    # たて
    for i in range(3):
        sc = [c[i % 3 + j * 3] for j in range(3)]
        if sc[0] == sc[1]:
            if p[i % 3 + 2 * 3] > max(p[i % 3], p[i % 3 + 3]):
                return False
        if sc[1] == sc[2]:
            if p[i % 3] > max(p[i % 3 + 3], p[i % 3 + 2 * 3]):
                return False
        if sc[2] == sc[0]:
            if p[i % 3 + 3] > max(p[i % 3 + 2 * 3], p[i % 3]):
                return False
    # 斜め
    if c[0] == c[4]:
        if p[8] > max(p[0], p[4]):
            return False
    if c[4] == c[8]:
        if p[0] > max(p[4], p[8]):
            return False
    if c[8] == c[0]:
        if p[4] > max(p[8], p[0]):
            return False

    if c[2] == c[4]:
        if p[6] > max(p[2], p[4]):
            return False
    if c[4] == c[6]:
        if p[2] > max(p[4], p[6]):
            return False
    if c[6] == c[2]:
        if p[4] > max(p[6], p[2]):
            return False
    return True


if __name__ == "__main__":
    main()
