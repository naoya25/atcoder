def is11_22_string(s):
    if len(s) % 2 == 0:
        return False

    mid = (len(s) + 1) // 2 - 1
    for i in range(mid):
        if s[i] != "1":
            return False

    if s[mid] != "/":
        return False

    for i in range(mid + 1, len(s)):
        if s[i] != "2":
            return False

    return True


def main():
    n = int(input())
    s = input()

    print("Yes" if is11_22_string(s) else "No")
    return


if __name__ == "__main__":
    main()
