def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    t = [list(input()) for _ in range(h)]
    ns = list(zip(*s[::-1]))
    nt = list(zip(*t[::-1]))
    ns.sort()
    nt.sort()
    if ns == nt:
        print("Yes")
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
