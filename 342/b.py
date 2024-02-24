def main():
    n = int(input())
    people = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        a, b = map(int, input().split())
        a_index, b_index = people.index(a), people.index(b)
        print(a if a_index < b_index else b)


if __name__ == "__main__":
    main()
