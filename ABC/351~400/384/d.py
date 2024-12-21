def main():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    # 累積和
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]
    sum_a = prefix[n]

    # 1周期内でsが作れる
    if sum_a > s:
        left = 0
        for right in range(1, n + 1):
            while left < right and prefix[right] - prefix[left] > s:
                left += 1
            if left < right and prefix[right] - prefix[left] == s:
                print("Yes")
                return

    heads_dict = {}
    for head in prefix[1:]:
        rem = head % sum_a
        if rem not in heads_dict or heads_dict[rem] > head:
            heads_dict[rem] = head

    for i in range(n):
        tail = sum_a - prefix[i]
        needed_rem = (s - tail) % sum_a
        if needed_rem in heads_dict:
            h_min = heads_dict[needed_rem]
            if tail + h_min <= s:
                print("Yes")
                return

    print("No")


if __name__ == "__main__":
    main()
