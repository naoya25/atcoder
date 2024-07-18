from collections import defaultdict


def main():
    n = int(input())
    p = list(map(int, input().split()))

    dd = defaultdict(int)
    for i in range(n):
        # 料理 p[i] を i-1,i,i+1 に移動させるための回数
        di1 = (p[i] - i - 1) % n
        di2 = (p[i] - i + 0) % n
        di3 = (p[i] - i + 1) % n

        dd[di1] += 1
        dd[di2] += 1
        dd[di3] += 1

    print(max(dd.values()))
    return


if __name__ == "__main__":
    main()
