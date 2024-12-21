def is1122_string(s):
    if len(s) % 2 != 0:
        return False

    s_set = set()
    for i in range(len(s) // 2):
        if s[2 * i] != s[2 * i + 1]:
            return False
        if s[2 * i] in s_set:
            return False
        s_set.add(s[2 * i])

    return True


def main():
    s = input()

    print("Yes" if is1122_string(s) else "No")
    return


if __name__ == "__main__":
    main()
