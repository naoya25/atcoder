def main():
    m = int(input())
    s1, s2, s3 = input(), input(), input()

    ans = float("inf")
    judge = False

    for i in range(m):
        for j in range(m):
            for k in range(m):
                if not (s1[i] == s2[j] == s3[k]):
                    continue
                judge = True
                t = max(i, j, k)
                if i == j == k:
                    t += 2 * m
                elif i == j or k == i:
                    t = i + m
                elif j == k:
                    t = j + m
                ans = min(ans, t)

    print(ans if judge else -1)
    return


if __name__ == "__main__":
    main()
