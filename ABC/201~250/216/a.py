def main():
    x, y = map(int, input().split("."))
    if 0 <= y <= 2:
        print(f"{x}-")
    elif 3 <= y <= 6:
        print(x)
    elif 7 <= y <= 9:
        print(f"{x}+")
    return


if __name__ == "__main__":
    main()
