def main():
    s_base = "wbwbwwbwbwbw"
    w, b = map(int, input().split())
    # s_baseのどれが1文字目にくるか
    for i in range(12):
        s = ""
        # 一致するかもしれない文字列作成
        for j in range(w + b):
            s += s_base[(i + j) % 12]
            if judge(s, w, b):
                print("Yes")
                return
    print("No")


def judge(s, w, b):
    if w == s.count("w") and b == s.count("b"):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
