def main():
    n, d = map(int, input().split())
    s = input()
    cnt = s.count("@")
    print(n - cnt + d)
    return


if __name__ == "__main__":
    main()
