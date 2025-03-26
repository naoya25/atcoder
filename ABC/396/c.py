from bisect import bisect_left, bisect_right


def main():
    n, m = map(int, input().split())
    black_list = list(map(int, input().split()))
    white_list = list(map(int, input().split()))
    black_list.sort()
    white_list.sort()

    black_zero_pos = n - bisect_left(black_list, 0)
    white_zero_pos = m - bisect_right(white_list, 0)

    black_list = black_list[::-1]
    white_list = white_list[::-1]

    ans = sum(black_list[:black_zero_pos]) + sum(white_list[:white_zero_pos])

    if black_zero_pos >= white_zero_pos:
        print(ans)
        return

    ans = sum(black_list[:black_zero_pos]) + sum(white_list[:black_zero_pos])
    for i in range(min(n, m) - black_zero_pos):
        c = black_zero_pos + i
        diff = black_list[c] + white_list[c]
        if diff <= 0:
            break
        ans += diff
    print(ans)
    return


if __name__ == "__main__":
    main()
