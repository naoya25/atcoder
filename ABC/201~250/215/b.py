import math


def main():
    n = int(input())
    k = int(math.log(n, 2))
    if 2**k > n:
        k -= 1
    print(k)
    return


if __name__ == "__main__":
    main()
