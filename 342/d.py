import math
from math import comb
from itertools import combinations
from collections import Counter


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    nums_count = Counter(nums)
    print(nums_count)
    combs = list(combinations(nums_count, 2))
    count = 0
    for a, b in combs:
        if is_square(a * b):
            count += nums_count[a] * nums_count[b]
    for a in nums_count.values():
        if a < 2:
            continue
        count += comb(a, 2)
    print(count)


def is_square(num):
    if num < 0:
        return False
    sqrt_num = math.isqrt(num)
    return sqrt_num * sqrt_num == num


if __name__ == "__main__":
    main()
