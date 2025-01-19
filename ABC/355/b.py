def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = a + b
    c.sort()

    ctn = 0
    for ci in c:
        if ci in a:
            ctn += 1
        else:
            ctn = 0
        if ctn >= 2:
            print("Yes")
            return
    print("No")
    return


if __name__ == "__main__":
    main()
