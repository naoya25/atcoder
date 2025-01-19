def main():
    n, m = map(int, input().split())
    s = list(input())
    c = list(map(int, input().split()))

    d = {i + 1: [] for i in range(m)}
    for i in range(n):
        d[c[i]].append(i)
    # print(d.values())

    for i_arr in d.values():
        len_i_arr = len(i_arr)
        n_arr = [0] * len_i_arr
        for i in range(len_i_arr):
            n_arr[(i + 1) % len_i_arr] = s[i_arr[i]]

        for i in range(len_i_arr):
            s[i_arr[i]] = n_arr[i]
    print("".join(s))
    return


if __name__ == "__main__":
    main()
