def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]

    bit_masks = []
    for i in range(n):
        bitmask = 0
        for j in range(m):
            if s[i][j] == "o":
                bitmask |= 1 << j
        bit_masks.append(bitmask)

    full_mask = (1 << m) - 1

    min_stalls = n + 1
    for mask in range(1, 1 << n):
        combined_mask = 0
        num_stalls = 0
        for i in range(n):
            if mask & (1 << i):
                combined_mask |= bit_masks[i]
                num_stalls += 1
        if combined_mask == full_mask:
            min_stalls = min(min_stalls, num_stalls)

    print(min_stalls)


if __name__ == "__main__":
    main()
