def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = 998244353
    ans = [0] * (n + 1)
    ans[1] = n
    ans[2] = n * (n - 1) // 2
    
    

    print(*ans[1:])

    return


if __name__ == "__main__":
    main()
