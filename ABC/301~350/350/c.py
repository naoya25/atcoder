def main():
    n = int(input())
    arr = list(map(int, input().split()))
    pos = {val: i for i, val in enumerate(arr, 1)}
    ans = []
    for i, val in enumerate(arr, 1):
        if val != i:
            j = pos[i]
            ans.append((min(i, j), max(i, j)))
            arr[j - 1] = val
            pos[val] = j

    print(len(ans))
    for i, j in ans:
        print(i, j)


if __name__ == "__main__":
    main()
