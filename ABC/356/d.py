def solve(N, M):
    MOD = 998244353
    total_sum = 0
    for i in range(M.bit_length()):
        if M & (1 << i):
            full_groups = (N + 1) // (1 << (i + 1))
            remainder = (N + 1) % (1 << (i + 1))
            count_of_1s = full_groups * (1 << i) + max(0, remainder - (1 << i))
            total_sum += count_of_1s
            total_sum %= MOD
    return total_sum


def main():
    n, m = map(int, input().split())

    print(solve(n, m))
    return


if __name__ == "__main__":
    main()
