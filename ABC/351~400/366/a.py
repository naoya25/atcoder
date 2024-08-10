def main():
    n, t, a = map(int, input().split())
    if abs(t - a) > n - (t + a):
        print("Yes")
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
