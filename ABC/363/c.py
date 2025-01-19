from more_itertools import distinct_permutations


def main():
    n, k = map(int, input().split())
    s = input()

    def j(i):  # 切り出した部分文字列の回文判定
        for j in range(k):
            if a[i + j] != a[i + k - 1 - j]:
                return False
        else:
            return True

    ans = 0
    for a in distinct_permutations(s):  # 10! = 3.6 * 10^6
        for i in range(n - k + 1):  # k部分文字列切り出し
            if j(i):
                break
        else:
            ans += 1

    print(ans)
    return


if __name__ == "__main__":
    main()
