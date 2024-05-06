def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_dic = {a[i]: i + 1 for i in range(n)}
    row = [a_dic[-1]]
    for _ in range(n - 1):
        row.append(a_dic[row[-1]])
    print(*row)


if __name__ == "__main__":
    main()
