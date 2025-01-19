import string


def main():
    n = int(input())
    s = input() + "*"
    if n == 1:
        print(1)
        return
    a = {c: 0 for c in string.ascii_lowercase}
    # print(a)
    nc, cnt = s[0], 1
    for c in s[1:]:
        if nc == c:
            cnt += 1
        else:
            a[nc] = max(a[nc], cnt)
            nc = c
            cnt = 1
    print(sum(a.values()))


if __name__ == "__main__":
    main()
