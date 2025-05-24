def main():
    a, b, c, d = map(int, input().split())
    time1 = a * 60 + b
    time2 = c * 60 + d

    if time1 > time2:
        print("Yes")
    else:
        print("No")

    return


if __name__ == "__main__":
    main()
