def main():
    n10 = int(input())
    n2 = list(bin(n10)[2:])

    idx = []
    for i in range(len(n2)):
        if n2[i] == "1":
            idx.append(i)

    for i in range(1 << len(idx)):
        new_n2 = n2.copy()
        for j in range(len(idx)):
            new_n2[idx[len(idx) - j - 1]] = str(i >> j & 1)
        print(int("".join(new_n2), 2))
    return


if __name__ == "__main__":
    main()
