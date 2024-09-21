import math


def main():
    m = int(input())

    ans = []

    while m != 0:
        ai = int(math.log(m, 3))
        m -= 3**ai
        ans.append(ai)

    print(len(ans))
    print(*ans)
    return


if __name__ == "__main__":
    main()
