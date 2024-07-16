from functools import cmp_to_key


def main():
    n = int(input())
    arr = []
    for i in range(1, n + 1):
        a, b = map(int, input().split())
        arr.append((-a, a + b, i))

    def compare(x, y):
        s = x[0] * y[1] - y[0] * x[1]
        if s > 0:
            return 1
        elif s < 0:
            return -1
        else:
            return 0

    sorted_arr = sorted(arr, key=cmp_to_key(compare))
    print(*[i[-1] for i in sorted_arr])


if __name__ == "__main__":
    main()
