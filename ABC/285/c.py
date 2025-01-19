import string


def main():
    s = input()
    a = string.ascii_uppercase
    l = len(a)
    d = {a[i]: i + 1 for i in range(l)}

    ans = 0
    for i in range(len(s)):
        ans += l**i * d[s[-i - 1]]
    print(ans)
    return


if __name__ == "__main__":
    main()
