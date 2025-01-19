def main():
    n = int(input())
    names = set([tuple(input().split()) for _ in range(n)])
    print("Yes" if len(names) != n else "No")
    return


if __name__ == "__main__":
    main()
