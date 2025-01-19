def compare_str(a, b):
    if len(a) < len(b):
        return -1
    elif len(a) > len(b):
        return 1
    else:
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0


def add_one(num_str):
    return str(int(num_str) + 1)


def is_good(s):
    ssum = sum(map(int, s))
    val = int(s)
    return val % ssum == 0


def main():
    n_str = input()
    twoN = str(int(n_str) * 2)
    LIMIT = 10**8

    s = n_str
    for _ in range(LIMIT + 1):
        if compare_str(s, twoN) > 0:
            break
        s_next = add_one(s)
        if compare_str(s_next, twoN) > 0:
            break

        if is_good(s) and is_good(s_next):
            print(s)
            return

        s = add_one(s)

    t = twoN
    for _ in range(LIMIT + 1):
        if compare_str(t, n_str) < 0:
            break
        t_prev_int = int(t) - 1
        if t_prev_int < 1:
            break
        t_prev = str(t_prev_int)
        if compare_str(t_prev, n_str) < 0:
            break

        if is_good(t_prev) and is_good(t):
            print(t_prev)
            return

        t = str(t_prev_int)

    print(-1)


if __name__ == "__main__":
    main()
