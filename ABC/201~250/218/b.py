import string


def main():
    p = list(map(int, input().split()))
    ans = ""
    for pi in p:
        ans += string.ascii_lowercase[pi - 1]
    print(ans)
    return


if __name__ == "__main__":
    main()
