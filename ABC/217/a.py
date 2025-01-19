def main():
    arr = input().split()
    sorted_arr = sorted(arr)
    if arr == sorted_arr:
        print("Yes")
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
