def main():
    s = input()
    if s == "0":
        print(0)
        return

    i = 0
    di = 0
    while i < len(s):
        if i + 1 < len(s) and s[i] == "0" and s[i + 1] == "0":
            di += 1
            i += 2
        else:
            i += 1

    print(len(s) - di)
    return


if __name__ == "__main__":
    main()
