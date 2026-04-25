def main():
    x, c = map(int, input().split())
    n = x // (1000 + c)
    print(1000 * n)
    return


if __name__ == "__main__":
    main()
