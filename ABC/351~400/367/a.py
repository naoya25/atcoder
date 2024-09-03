def main():
    a, b, c = map(int, input().split())

    if b > c:
        b -= 24

    if b < a < c:
        print("No")
    else:
        print("Yes")

    return


if __name__ == "__main__":
    main()
