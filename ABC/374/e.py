def main():
    n, x = map(int, input().split())
    processes = [tuple(map(int, input().split())) for _ in range(n)]

    left, right = 0, 10**9

    while left <= right:
        mid = (left + right) // 2
        if can_achieve(mid, processes, x):
            left = mid + 1
        else:
            right = mid - 1

    print(left, mid, right)
    print(can_achieve(left, processes, x))
    if can_achieve(left, processes, x):
        print(left)
    else:
        print(right)


def can_achieve(w, processes, x):
    total_cost = 0
    for a, p, b, q in processes:
        cost_per_a = p / a
        cost_per_b = q / b

        if cost_per_a < cost_per_b:
            num_s = w // a
            remaining_w = w - num_s * a
            total_cost += num_s * p

            if remaining_w > 0:
                num_t = -(-remaining_w // b)
                total_cost += num_t * q
        else:

            num_t = w // b
            remaining_w = w - num_t * b
            total_cost += num_t * q

            if remaining_w > 0:
                num_s = -(-remaining_w // a)
                total_cost += num_s * p

        if total_cost > x:
            return False

    return True


if __name__ == "__main__":
    main()
