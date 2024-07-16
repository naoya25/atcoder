def main():
    a, b = map(int, input().split())
    if a == b:
        print(-1)
        return
    else:
        print(6 - a - b)
    return


if __name__ == "__main__":
    main()
