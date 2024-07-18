from collections import defaultdict


def main():
    n = int(input())

    dd = defaultdict(int)
    for _ in range(n):
        s = input()
        if dd[s] == 0:
            print(s)
        else:
            print(f"{s}({dd[s]})")

        dd[s] += 1
    return


if __name__ == "__main__":
    main()
