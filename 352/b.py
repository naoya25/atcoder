def main():
    s = input()
    t = input()

    idx = 0
    ans = []
    for i, ti in zip(range(len(t)), t):
        if ti == s[idx]:
            idx += 1
            ans.append(i + 1)
    print(*ans)


if __name__ == "__main__":
    main()
