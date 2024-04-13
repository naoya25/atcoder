import re


def main():
    s = input()
    t = list(input().lower())

    pattern = r".*?" + r".*?".join(t)
    if t[-1] == "x":
        pattern_x = r".*?" + r".*?".join(t[:-1])
        if re.match(pattern_x, s):
            print("Yes")
        else:
            print("No")
        return

    if re.match(pattern, s):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
