def main():
    n = int(input())
    h = list(map(int, input().split()))

    t = 0
    idx = 0  # 1,1,3の攻撃の何番目か
    for hi in h:
        t += (hi // 5) * 3
        a = hi % 5
        if a == 0:
            continue
        elif a == 1:
            t += 1
            if idx == 0 or idx == 1:
                idx += 1
            else:
                idx = 0
        elif a == 2:
            if idx == 0:
                idx = 2
                t += 2
            elif idx == 1:
                idx = 0
                t += 2
            else:
                idx = 0
                t += 1
        elif a == 3:
            if idx == 0:
                idx = 0
                t += 3
            elif idx == 1:
                idx = 0
                t += 2
            else:
                idx = 0
                t += 1
        else:
            if idx == 0:
                idx = 0
                t += 3
            elif idx == 1:
                idx = 0
                t += 2
            else:
                idx = 1
                t += 2
    print(t)
    return


if __name__ == "__main__":
    main()
