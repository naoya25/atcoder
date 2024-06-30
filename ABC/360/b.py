def main():
    s, t = input().split()
    ls, lt = len(s), len(t)  # 7, 3

    for w in range(1, ls):
        if lt - 1 <= ls // w <= lt:
            for c in range(w):
                if judge(s, t, w, c):
                    print("Yes")
                    return
    print("No")
    return


def judge(s, t, w, c):
    character = ""
    for i in range(c, len(s), w):
        character += s[i]
    return character == t


if __name__ == "__main__":
    main()
