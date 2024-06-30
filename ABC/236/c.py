def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()

    j = 0
    for ti in t:
        for i in range(j, n):
            if s[i] == ti:
                print("Yes")
                j = i + 1
                break
            else:
                print("No")

    return


if __name__ == "__main__":
    main()
