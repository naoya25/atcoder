def main():
    n = int(input())

    for _ in range(n):
        a_list = list(map(int, input().split()))
        print(*[i+1 for i, e in enumerate(a_list) if e == 1])


if __name__ == "__main__":
    main()
