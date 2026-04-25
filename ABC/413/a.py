def main():
    n, m = map(int, input().split())
    a = sum(list(map(int, input().split())))
    if a <= m:
        print("Yes")
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
