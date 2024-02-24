def main():
    s = input()

    for i, c in enumerate(s):
        if s.count(c) == 1:
            print(i + 1)
            return


if __name__ == "__main__":
    main()
