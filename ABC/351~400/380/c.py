from itertools import groupby


def main():
    n, k = map(int, input().split())
    s = input()

    arr = [len(list(g)) for _, g in groupby(s)]

    idx = 2 * k - 1 if s[0] == "0" else 2 * (k - 1)

    arr[idx - 2] += arr[idx]
    arr[idx - 1] += arr[idx + 1] if idx + 1 < len(arr) else 0
    arr[idx] = 0
    if idx + 1 < len(arr):
        arr[idx + 1] = 0

    ans = []
    cs = "1" if s[0] == "1" else "0"
    for r in arr:
        ans.append(cs * r)
        cs = "1" if cs == "0" else "0"
    print("".join(ans))
    return


if __name__ == "__main__":
    main()
