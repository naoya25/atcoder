def main():
    l, r = map(int, input().split())

    current_num = l
    while current_num <= r:
        n = current_num + 1
        while n <= r and judge(current_num, n):
            n += 1

        print(current_num, n)
        current_num = n


def judge(a, b):  # S(a, b) が良い数列か判定
    i = 0
    while True:
        j = 0
        while True:
            if (a == (1 << i) * j) and (b == (1 << i) * (j + 1)):
                return True
            j += 1
            if (1 << i) * j > b:
                break
        i += 1
        if (1 << i) > b:
            return False


if __name__ == "__main__":
    main()
