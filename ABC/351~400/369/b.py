def main():
    n = int(input())
    r_arr = []
    l_arr = []
    for _ in range(n):
        a, s = input().split()
        a = int(a)
        if s == "L":
            l_arr.append(a)
        else:
            r_arr.append(a)
    # print(r_arr)
    # print(l_arr)
    ans = 0
    ans += sum_diff(r_arr)
    ans += sum_diff(l_arr)
    print(ans)
    return


def sum_diff(arr):
    cnt = 0
    for i in range(len(arr) - 1):
        cnt += abs(arr[i] - arr[i + 1])
    return cnt


if __name__ == "__main__":
    main()
