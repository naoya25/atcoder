def main():
    s = list(input())
    del s[len(s) // 2]
    print("".join(s))

    return


if __name__ == "__main__":
    main()
