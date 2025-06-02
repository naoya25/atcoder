def main():
    n, s = map(int, input().split())
    t = list(map(int, input().split()))
    td = 0
    for i in range(n):
        if t[i] - td > s:
            print("No")
            return
        td = t[i]
    else:
        print("Yes")
    return


if __name__ == "__main__":
    main()
