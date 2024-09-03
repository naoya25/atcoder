def main():
    a, b = map(int, input().split())
    if a == b:
        print(1)
    elif abs(a - b) % 2 != 0:
        print(2)
    else:
        print(3)

    return


if __name__ == "__main__":
    main()
