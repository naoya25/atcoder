def judge(n):
    if n == 1:
        return True
    while n % 2 == 0:
        n /= 2
    while n % 3 == 0:
        n /= 3

    return n == 1

if __name__ == '__main__':
    n = int(input())
    print('Yes' if judge(n) else 'No')
