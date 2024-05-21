def main():
    n = int(input())
    s = []
    t = 0
    for _ in range(n):
        s_i, c = input().split()
        s.append(s_i)
        t += int(c)
    s.sort()
    # print(s)
    print(s[t % n])
    return


if __name__ == "__main__":
    main()
