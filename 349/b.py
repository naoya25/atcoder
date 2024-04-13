def main():
    s = input()
    s_counts = {}

    for c in set(s):
        c_count = s.count(c)
        if c_count in s_counts.keys():
            s_counts[c_count] += 1
        else:
            s_counts[c_count] = 1

    for k, v in s_counts.items():
        if not (v == 0 or v == 2):
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()
