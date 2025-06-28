def main():
    n = int(input())
    t = input()
    a = input()

    for i in range(n):
        if t[i] == a[i] == "o":
            print("Yes")
            return

    print("No")
    return


if __name__ == "__main__":
    main()
