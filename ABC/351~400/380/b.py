def main():
    s = input()
    s_arr = s.split("|")
    print(*[len(i) for i in s_arr[1:-1]])
    return


if __name__ == "__main__":
    main()
