def main():
    n_str, c1, c2 = input().split()
    s = list(input())
    for i in range(len(s)):
        if s[i] != c1:
            s[i] = c2

    print("".join(s))
    return


if __name__ == "__main__":
    main()
