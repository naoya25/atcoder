def main():
    a, b, c, d, e = map(int, input().split())
    ans = {}
    for mask in range(1 << 5):
        key = ""
        total = 0
        if mask & 1:
            key += "A"
            total += a
        if mask & 2:
            key += "B"
            total += b
        if mask & 4:
            key += "C"
            total += c
        if mask & 8:
            key += "D"
            total += d
        if mask & 16:
            key += "E"
            total += e
        ans[key] = total
    sorted_ans = sorted(ans.items(), key=lambda x: (-x[1], x[0]))
    for key, value in sorted_ans:
        if key != "":
            print(key)
    return


if __name__ == "__main__":
    main()
