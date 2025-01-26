def main():
    a = list(map(int, input().split()))
    n = len(a)
    for i in range(n - 1):
        a[i], a[i + 1] = a[i + 1], a[i]
        if a == sorted(a):
            print("Yes")
            return
        a[i], a[i + 1] = a[i + 1], a[i]
    print("No")


if __name__ == "__main__":
    main()
