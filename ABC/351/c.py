def main():
    n = int(input())
    balls = list(map(int, input().split()))

    row = []

    for ball in balls:
        row.append(ball)

        while len(row) >= 2:
            if row[-1] != row[-2]:
                break
            else:
                b1 = row.pop()
                b2 = row.pop()

                row.append(b1 + 1)
        # print(row)

    print(len(row))


if __name__ == "__main__":
    main()
