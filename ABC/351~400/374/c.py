def main():
    n = int(input())
    k = list(map(int, input().split()))

    # bit全探索
    ans = float("inf")
    for bit in range(1 << n):
        group_a = 0
        group_b = 0
        for i in range(n):
            if bit & (1 << i):
                group_a += k[i]
            else:
                group_b += k[i]

        ans = min(ans, max(group_a, group_b))
    print(ans)
    return


if __name__ == "__main__":
    main()
