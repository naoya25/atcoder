def main():
    r = int(input())
    j = r - 1
    quadrant = 0
    for i in range(1, r):
        while r**2 < (i + 0.5) ** 2 + (j + 0.5) ** 2:
            j -= 1
        quadrant += j

    print((r - 1) * 4 + 1 + quadrant * 4)


if __name__ == "__main__":
    main()
