def count_trailing_a(s):
    count = 0
    for char in reversed(s):
        if char == "a":
            count += 1
        else:
            break
    return count


def count_leading_a(s):
    count = 0
    for char in s:
        if char == "a":
            count += 1
        else:
            break
    return count


def main():
    s = input()

    nr = count_trailing_a(s)
    nl = count_leading_a(s)

    s = s.rstrip("a")
    s = s.lstrip("a")

    if nl > nr:
        print("No")
        return

    if s == s[::-1]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
