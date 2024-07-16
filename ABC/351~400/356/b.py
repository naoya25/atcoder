def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(n):
        x = list(map(int, input().split()))
        for j in range(m):
            a[j] -= x[j]

    if all(x <= 0 for x in a):
        print("Yes")
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
