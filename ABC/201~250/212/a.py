def main():
    a, b = map(int, input().split())
    if 0 < a and 0 < b:
        print("Alloy")
    elif 0 < a:
        print("Gold")
    else:
        print("Silver")

    return


if __name__ == "__main__":
    main()
