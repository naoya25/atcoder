def main():
    n = int(input())
    s = "oox"
    print(s * (n // 3) + s[: n % 3])


if __name__ == "__main__":
    main()
