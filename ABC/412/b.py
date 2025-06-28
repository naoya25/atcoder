def main():
    s = input()
    t = input()

    for i in range(1, len(s)):
        if s[i].isupper():
            if s[i - 1] not in t:
                print("No")
                return
    print("Yes")
    return


if __name__ == "__main__":
    main()
