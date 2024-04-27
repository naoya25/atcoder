def main():
    n, a, b = map(int, input().split())
    d_list = sorted(set(map(lambda x: int(x) % (a + b), input().split())))
    # print(d_list)

    max_diff = 0
    for i in range(len(d_list) - 1):
        diff = d_list[i + 1] - d_list[i] - 1
        max_diff = max(max_diff, diff)
    max_diff = max(max_diff, d_list[0] - d_list[-1] + a + b - 1)  # 次の週に跨ぐ場合

    # print(max_diff)
    print("Yes" if max_diff >= b else "No")


if __name__ == "__main__":

    main()
