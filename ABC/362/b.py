def main():
    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xc, yc = map(int, input().split())

    ab2 = (xb - xa) ** 2 + (yb - ya) ** 2
    bc2 = (xc - xb) ** 2 + (yc - yb) ** 2
    ca2 = (xa - xc) ** 2 + (ya - yc) ** 2

    if ab2 + bc2 == ca2 or bc2 + ca2 == ab2 or ca2 + ab2 == bc2:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
