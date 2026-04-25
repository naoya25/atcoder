def main():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        maximum = min(a, c)
        if maximum < 1:
            print(0)
            continue

        if b >= maximum:
            print(maximum)
        else:
            print(min((a + b + c) // 3, maximum))

    return


if __name__ == "__main__":
    main()
