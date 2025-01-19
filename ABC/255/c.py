def main():
    x, a, d, n = map(int, input().split())
    if d == 0:
        print(abs(x - a))
        return

    i = (x - a) // d + 1
    if 1 <= i < n:
        print(min(abs(x - (a + i * d)), abs(x - (a + (i - 1) * d))))
    elif i <= 0:
        print(abs(x - a))
    else:
        print(abs(x - (a + (n - 1) * d)))
    return


if __name__ == "__main__":
    main()
