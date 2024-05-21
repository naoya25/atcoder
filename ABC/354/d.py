def main():
    a, b, c, d = map(int, input().split())
    base = [0, 0.5, 1, 0.5]
    w = c - a
    h = d - b
    ans = -(-(w * h) // 2)
    # if (w * h) % 2 == 0:
    #     ans += 1
    print(ans)

    return


if __name__ == "__main__":
    main()
