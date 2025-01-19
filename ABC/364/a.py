def main():
    n = int(input())
    j = [False] * n
    _s = ""
    for i in range(n):
        s = input()
        j[i] = True
        if s == _s == "sweet":
            break
        _s = s
    # print(j)
    if all(j):
        print("Yes")
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
