def main():
    n, q = map(int, input().split())
    teeth = [1] * n
    t_list = list(map(int, input().split()))
    for t in t_list:
        teeth[t - 1] = 1 if teeth[t - 1] == 0 else 0
    print(sum(teeth))


if __name__ == "__main__":
    main()
