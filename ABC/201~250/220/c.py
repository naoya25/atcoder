def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    a_sum = sum(a)
    ans = (x // a_sum) * n
    x = x % a_sum
    for i in range(n):
        if x >= a[i]:
            x -= a[i]
        else:
            ans += i + 1
            break
    print(ans)
    return


if __name__ == "__main__":
    main()
