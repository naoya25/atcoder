import math


def main():
    n = int(input())
    cube_base = math.ceil((n + 1) ** (1 / 3))  # N以下の最大の立方根

    for i in range(cube_base):
        cube = (cube_base - i) ** 3
        if is_palindrome(cube):
            if cube <= n:
                print(cube)
                return


def is_palindrome(n):
    return int(n) == int(str(n)[::-1])


if __name__ == "__main__":
    main()
