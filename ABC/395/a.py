def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n-1):
        if a[i] >= a[i+1]:
            print('No')
            return
    else:
        print('Yes')
    return


if __name__ == "__main__":
    main()
