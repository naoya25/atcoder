def main():
    sx, sy = map(int, input().split())
    tx, ty = map(int, input().split())

    if (sx + sy) % 2 == 1:
        sx -= 1

    if (tx + ty) % 2 == 1:
        tx -= 1

    dx = abs(sx - tx)
    dy = abs(sy - ty)
    ans = (dy + max(dx, dy)) // 2
    print(ans)

    return


if __name__ == "__main__":
    main()
