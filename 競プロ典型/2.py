def main():
    n = int(input())
    if n % 2 == 1:
        return
    s1, s2 = "(", ")"

    def judge(bit):
        cnt = 0
        s = ""
        for i in range(n):
            if bit & (1 << i):
                cnt += 1
                s += s1
            else:
                if cnt < 1:
                    return False, ""
                cnt -= 1
                s += s2
        if cnt == 0:
            return True, s
        else:
            return False, ""

    ans = []
    for bit in range(1 << n):
        j, s = judge(bit)
        if j:
            ans.append(s)

    ans.sort()
    for r in ans:
        print(r)
    return


if __name__ == "__main__":
    main()
