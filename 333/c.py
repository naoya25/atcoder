def main():
    n = int(input())

    ans = [3]  # 逆順
    for _ in range(n - 1):
        if ans[-1] == 3:
            ans.append(1)
            for i in range(1, len(ans)):
                ans[i] = 1
            continue

        for i in range(len(ans)):
            if ans[i] == 3:
                continue
            ans[i] += 1
            if ans[i] == 2:
                for j in range(1, i):
                    ans[j] = 2
            break

    print("".join(map(str, ans[::-1])))


if __name__ == "__main__":
    main()
