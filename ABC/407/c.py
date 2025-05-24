def main():
    s = input()
    n = len(s)

    x_next = int(s[-1])
    for i in range(n - 2, -1, -1):
        si = int(s[i])
        diff = x_next - si
        if diff <= 0:
            x_curr = si
        else:
            x_curr = si + ((diff + 9) // 10) * 10
        x_next = x_curr

    print(n + x_next)

    return


if __name__ == "__main__":
    main()
