def main():
    n = int(input())
    a_list = tuple(map(int, input().split()))
    m = int(input())
    b_list = tuple(map(int, input().split()))
    L = int(input())
    c_list = tuple(map(int, input().split()))
    q = int(input())
    x_list = tuple(map(int, input().split()))

    comb = set()
    for a in a_list:
        for b in b_list:
            for c in c_list:
                comb.add(a + b + c)

    for x in x_list:
        print("Yes" if x in comb else "No")


if __name__ == "__main__":
    main()
