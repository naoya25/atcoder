def main():
    n, m = map(int, input().split())
    present_numbers = set(map(int, input().split()))

    print(n - m)

    print(*[i for i in range(1, n + 1) if i not in present_numbers])


if __name__ == "__main__":
    main()
