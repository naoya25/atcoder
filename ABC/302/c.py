from itertools import permutations


def main():
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    perm = list(permutations(arr))
    for p in perm:  # n! 8!
        for i in range(1, n):  # n-1
            cnt = 0
            for s1, s2 in zip(p[i - 1], p[i]):  # m
                if s1 == s2:
                    cnt += 1
            if cnt != m - 1:
                break
        else:
            print("Yes")
            return
    print("No")
    return


if __name__ == "__main__":
    main()
