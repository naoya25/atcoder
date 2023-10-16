def remove_s_index(s, i):
    if 0 <= i < len(s):
        result = s[:i] + s[i + 1:]
        return result

def main(n, t1, lent1):
    similars = []
    for i in range(n):
        s = input()
        lens = len(s)

        if s == t1:
            similars.append(i + 1)
        elif lens == lent1:
            diff_count = 0
            for s1, s2 in zip(s, t1):
                if s1 != s2:
                    diff_count += 1
                    if diff_count > 1:
                        break
            if diff_count <= 1:
                similars.append(i + 1)
        elif abs(lens - lent1) == 1:
            if lens > lent1:
                s1, s2 = s, t1 # s1が大きい方
            else:
                s1, s2 = t1, s
            for s_i in range(len(s1)):
                if remove_s_index(s1, s_i) == s2:
                    similars.append(i + 1)
                    break
    return similars

if __name__ == '__main__':
    n, t1 = input().split()
    n = int(n)
    output = main(n, t1, len(t1))
    print(len(output))
    if len(output) > 0:
        print(*output)
