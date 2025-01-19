def main():
    s = input()
    mi = s.index("M")
    ri = s.index("R")
    print("Yes" if mi > ri else "No")
    return


if __name__ == "__main__":
    main()
