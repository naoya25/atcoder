def main():
    s = input()
    num = int(s[3:])
    if num == 316:
        print("No")
        return
    print("Yes" if 1 <= num <= 349 else "No")


if __name__ == "__main__":
    main()
