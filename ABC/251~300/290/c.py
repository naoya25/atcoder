def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(list(set(a))) + [-1] * k

    def mex(x):
        for i in range(k):
            if i != x[i]:
                return i
        return i + 1

    print(mex(a[:k]))
    return


if __name__ == "__main__":
    main()
