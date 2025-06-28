def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        solve(n, s)


def solve(n, s):
    if n == 1:
        print(s)
        return

    alpha = [ord(char) - ord("a") for char in s]
    l = 0
    for i in range(n - 1):
        if alpha[i] > alpha[i + 1]:
            l = i
            break
    r = n - 1
    for i in range(l, n):
        if alpha[i] > alpha[l]:
            r = i - 1
            break

    print(cyclic_shift_left(s, l, r))


def cyclic_shift_left(s, l, r):
    substring = s[l : r + 1]
    shifted = substring[1:] + substring[0]
    result = s[:l] + shifted + s[r + 1 :]
    return result


if __name__ == "__main__":
    main()
