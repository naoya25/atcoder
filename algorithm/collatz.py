def collatz(n, memo):
    current_memo = set()
    while n != 1:
        current_memo.add(n)
        if n in memo:
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    return True, memo | current_memo


def main():
    n = 1
    memo = set()

    while True:
        result, memo = collatz(n, memo)
        if result:
            print(n)
        n += 1


if __name__ == "__main__":
    main()
