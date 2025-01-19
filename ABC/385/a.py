def main():
    arr = list(map(int, input().split()))
    arr.sort()
    if arr[0] + arr[1] == arr[2] or arr[0] == arr[1] == arr[2]:
        print("Yes")
    else:
        print("No")

    return


if __name__ == "__main__":
    main()
