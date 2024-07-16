def main():
    n = int(input())
    slot = [input() for _ in range(n)]

    ans = float("inf")

    for i in range(n):
        for t in range(10):
            num = slot[i][t]  # numを全てのスロットで止める
            dt = [t]
            for j in range(n):
                if i == j:
                    continue
                di = slot[j].index(num)
                while di <= t or di in dt:
                    di += 10
                dt.append(di)

            ans = min(ans, max(dt))
    print(ans)
    return


if __name__ == "__main__":
    main()
