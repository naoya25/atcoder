def main():
    n = int(input())
    t = []  # s
    a_arr = []  # cm
    b_arr = []  # cm/s
    for _ in range(n):
        a, b = map(int, input().split())
        t.append(a / b)
        a_arr.append(a)
        b_arr.append(b)
    mt = sum(t) / 2
    nt = 0
    for i in range(n):
        nt += t[i]
        if nt >= mt:
            print(sum(a_arr[: i + 1]) - b_arr[i] * (nt - mt))
            return

    return


if __name__ == "__main__":
    main()
