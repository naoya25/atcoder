def main():
    x = input()
    n = int(input())
    s = [input() for _ in range(n)]

    sort_dict = {a: i for i, a in enumerate(x)}
    sort_key = lambda a: [sort_dict[char] for char in a]

    for e in sorted(s, key=sort_key):
        print(e)
    return


if __name__ == "__main__":
    main()
