def main():
    n = int(input())
    l_arr, r_arr = [], []
    size = []
    for _ in range(n):
        l, r = map(int, input().split())
        l_arr.append(l)
        r_arr.append(r)
        size.append(r - l)

    if sum(l_arr) > 0 or sum(r_arr) < 0:
        print("No")
        return
    print("Yes")

    gap = -sum(l_arr)
    ans = []
    for i in range(n):
        if gap >= size[i]:
            ans.append(l_arr[i] + size[i])
            gap -= size[i]
        else:
            ans.append(l_arr[i] + gap)
            gap = 0

    print(*ans)
    return


if __name__ == "__main__":
    main()
