from bisect import bisect_left, bisect_right


def main():
    n, t = map(int, input().split())
    s = input()
    x = list(map(int, input().split()))

    positive, negative = [], []
    for i in range(n):
        if s[i] == "0":
            negative.append(x[i])
        else:
            positive.append(x[i])
    positive.sort()
    negative.sort()

    result = 0
    for x in positive:
        left = bisect_left(negative, x)
        right = bisect_right(negative, x + 2 * t)
        result += right - left
    print(result)

    return


if __name__ == "__main__":
    main()
