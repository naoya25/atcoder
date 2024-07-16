def main():
    n = int(input())
    s_set = set()
    for _ in range(n):
        s = input()
        if s[::-1] not in s_set:
            s_set.add(s)
    print(len(s_set))
    return


if __name__ == "__main__":
    main()
