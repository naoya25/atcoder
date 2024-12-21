def max_distinct_pairs(a, start):
    n = len(a)
    seen = set()
    left = start
    max_length = 0
    for right in range(start, n - 1, 2):
        while (a[right] != a[right + 1] or a[right] in seen) and left <= right:
            if a[left] == a[left + 1]:
                seen.remove(a[left])
            left += 2

        if a[right] == a[right + 1] and a[right] not in seen:
            seen.add(a[right])
            current_length = right - left + 2
            max_length = max(max_length, current_length)

    return max_length


def main():
    n = int(input())
    a = tuple(map(int, input().split()))

    even_max = max_distinct_pairs(a, 0)
    odd_max = 0
    if n > 1:
        odd_max = max_distinct_pairs(a, 1)

    print(max(even_max, odd_max))


if __name__ == "__main__":
    main()
