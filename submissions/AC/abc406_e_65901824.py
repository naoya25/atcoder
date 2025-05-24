# URL: https://atcoder.jp/contests/abc406/submissions/65901824
# id: 65901824
# epoch_second: 1747486502
# problem_id: abc406_e
# contest_id: abc406
# user_id: naoya1
# language: Python (PyPy 3.10-v7.3.12)
# point: 450.0
# length: 1483
# result: AC
# execution_time: 99


# submitted code
def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        ans = calc_ans(n, k)
        print(ans)
    return


def calc_ans(n, k):
    m = 998244353
    bits = bin(n)[2:]
    L = len(bits)

    cnt = [[0, 0] for _ in range(k + 2)]
    sm = [[0, 0] for _ in range(k + 2)]
    cnt[0][1] = 1

    for i, ch in enumerate(bits):
        bN = int(ch)
        w = pow(2, L - 1 - i, m)
        nxt_cnt = [[0, 0] for _ in range(k + 2)]
        nxt_sm = [[0, 0] for _ in range(k + 2)]

        for ones in range(k + 1):
            for tight in (0, 1):
                c = cnt[ones][tight]
                s = sm[ones][tight]
                if c == 0:
                    continue
                max_bit = bN if tight else 1
                for bit in (0, 1):
                    if bit > max_bit:
                        continue
                    n_ones = ones + bit
                    if n_ones > k:
                        continue
                    ntight = tight & (bit == max_bit)
                    nc = nxt_cnt[n_ones][ntight]
                    ns = nxt_sm[n_ones][ntight]

                    nc = (nc + c) % m
                    ns = (ns + s + bit * w * c) % m
                    nxt_cnt[n_ones][ntight] = nc
                    nxt_sm[n_ones][ntight] = ns

        cnt, sm = nxt_cnt, nxt_sm

    return (sm[k][0] + sm[k][1]) % m


if __name__ == "__main__":
    main()
