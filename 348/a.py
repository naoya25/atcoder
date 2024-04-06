def main():
    n = int(input())
    result = ""
    for i in range(n):
        if i % 3 == 2:
            result += "x"
        else:
            result += "o"

    print(result)


if __name__ == "__main__":
    main()
