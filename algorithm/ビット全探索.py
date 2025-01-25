def main():
    n = int(input())
    items = ["a", "b", "c"]

    for bit in range(1 << n):
        subset = []
        for i in range(n):
            if bit & (1 << i):
                subset.append(items[i])
        print(subset)


if __name__ == "__main__":
    main()
