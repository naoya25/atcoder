def main():
    n, k = map(int, input().split())
    p = [0] * n
    for i in range(n):
        p[i] = sum(map(int, input().split()))

    sp = sorted(p, reverse=True)[k-1]


    for i in range(n):
        if p[i] + 300 >= sp:
            print("Yes")
        else:
            print("No")

    return


if __name__ == "__main__":
    main()
