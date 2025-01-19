def main():
    x = int(input())
    t = 1
    n = 1
    while n != x:
        t += 1
        n *= t
    print(t)
    return


if __name__ == "__main__":
    main()
