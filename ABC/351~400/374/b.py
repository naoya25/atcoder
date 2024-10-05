def main():
    s = input()
    t = input()
    if s == t:
        print(0)
        return
    min_len = min(len(s), len(t))

    for i in range(min_len):
        if s[i] != t[i]:
            print(i + 1)
            return
    else:
        print(min_len + 1)
    return


if __name__ == "__main__":
    main()
