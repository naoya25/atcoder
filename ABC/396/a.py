def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n - 2):
        if a[i] == a[i + 1] == a[i + 2]:
            print("Yes")
            return
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
