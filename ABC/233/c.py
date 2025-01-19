import itertools
import functools
import operator


def main():
    n, x = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split()))[1:])

    ans = 0
    for p in itertools.product(*a):
        if x == functools.reduce(operator.mul, p):
            ans += 1
    print(ans)
    return


if __name__ == "__main__":
    main()
