def main():
    a, b = map(int, input().split())
    c = a / b
    d = a // b
    if c - d > d + 1 - c:
        print(d + 1)
    else:
        print(d)
    return


if __name__ == "__main__":
    main()
