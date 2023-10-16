# TLE
def main(n, t1, lent1):
    similars = []
    for i in range(n):
        s = input().strip()
        lens = len(s)

        if s == t1:
            similars.append(i + 1)
        elif lens == lent1:
            diff_count = sum(1 for s1, s2 in zip(s, t1) if s1 != s2)
            if diff_count <= 1:
                similars.append(i + 1)
        elif abs(lens - lent1) == 1:
            if lens > lent1:
                s1, s2 = s, t1
            else:
                s1, s2 = t1, s
            if any(s1[:s_i] + s1[s_i + 1:] == s2 for s_i in range(len(s1))):
                similars.append(i + 1)
    return similars

if __name__ == '__main__':
    n, t1 = input().split()
    n = int(n)
    output = main(n, t1, len(t1))
    print(len(output))
    if len(output) > 0:
        print(*output)
