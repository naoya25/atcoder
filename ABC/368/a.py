def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a_ = a[n - k :] + a[: n - k]
    print(*a_)
    return


if __name__ == "__main__":
    main()
