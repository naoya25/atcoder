def main():
    n, m = map(int, input().split())
    schedule = [int(input()) for _ in range(m)]

    parade_count = [0] * (n + 1)
    distinct_parades = 0
    left_pointer = 0

    min_days = 100000

    for right_pointer in range(m):
        parade = schedule[right_pointer]

        if parade_count[parade] == 0:
            distinct_parades += 1

        parade_count[parade] += 1

        while distinct_parades == n:
            min_days = min(min_days, right_pointer - left_pointer + 1)
            left_parade = schedule[left_pointer]

            parade_count[left_parade] -= 1
            if parade_count[left_parade] == 0:
                distinct_parades -= 1

            left_pointer += 1

    print(min_days)


if __name__ == "__main__":
    main()
