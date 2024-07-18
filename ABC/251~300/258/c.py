def main():
    n, q = map(int, input().split())
    s = input()
    dx = 0
    for _ in range(q):
        qi,x = map(int, input().split())
        if qi == 1:
            dx += x
        else:
            print(s[(x - dx - 1) % n])
    return


if __name__ == "__main__":
    main()
