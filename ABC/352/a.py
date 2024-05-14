def main():
    n, x, y, z = map(int, input().split())
    print("Yes" if min(x, y) <= z <= max(x, y) else "No")


if __name__ == "__main__":
    main()
