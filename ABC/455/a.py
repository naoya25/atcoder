def main():
    a, b, c = map(int, input().split())
    if a != b and b == c:
        print("Yes")
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
