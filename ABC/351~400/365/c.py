def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    if m >= sum(a):
        print("infinite")
        return

    a.sort()
    total_sum = 0

    for i in range(n):
        additional_cost = (a[i] - (a[i - 1] if i > 0 else 0)) * (n - i)
        if total_sum + additional_cost > m:
            ans = (m - total_sum) // (n - i) + (a[i - 1] if i > 0 else 0)
            print(ans)
            return
        total_sum += additional_cost

    print(a[-1])


if __name__ == "__main__":
    main()
