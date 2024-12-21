# def is11_22_string(s):
#     if len(s) % 2 == 0:
#         return False

#     mid = (len(s) + 1) // 2 - 1
#     for i in range(mid):
#         if s[i] != "1":
#             return False

#     if s[mid] != "/":
#         return False

#     for i in range(mid + 1, len(s)):
#         if s[i] != "2":
#             return False

#     return True


def main():
    n = int(input())
    s = input()

    max_length = 0
    for i in range(len(s)):
        if s[i] != "/":
            continue
        left = i - 1
        right = i + 1
        count_ones = 0
        count_twos = 0

        while left >= 0 and s[left] == "1":
            count_ones += 1
            left -= 1

        while right < len(s) and s[right] == "2":
            count_twos += 1
            right += 1

        t = min(count_ones, count_twos)
        current_length = 2 * t + 1

        max_length = max(max_length, current_length)

    print(max_length)
    return


if __name__ == "__main__":
    main()
