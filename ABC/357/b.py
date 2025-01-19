def main():
    s = input()
    up = sum(1 for c in s if c.isupper())
    low = sum(1 for c in s if c.islower())

    if up > low:
        print(s.upper())
    else:
        print(s.lower())
    return


if __name__ == "__main__":
    main()
