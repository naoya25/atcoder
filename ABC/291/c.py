def main():
    n = int(input())
    s = input()

    directions = {"R": (1, 0), "L": (-1, 0), "D": (0, -1), "U": (0, 1)}
    nx, ny = 0, 0
    d = set([(0, 0)])
    for si in s:
        dx, dy = directions[si]
        nx += dx
        ny += dy
        if (nx, ny) in d:
            print("Yes")
            return
        d.add((nx, ny))

    print("No")
    return


if __name__ == "__main__":
    main()
