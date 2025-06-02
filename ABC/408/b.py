def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(set(a))
    print(len(a))
    print(*a)
    return


if __name__ == "__main__":
    main()
