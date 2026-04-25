def main():
    n = int(input())
    a = [1, 1]
    for i in range(n - 1):
        a.append(a[-1] + f(a[-1]))
    print(a[-1])
    return


def f(n):
    return sum(int(d) for d in str(n))


if __name__ == "__main__":
    main()
