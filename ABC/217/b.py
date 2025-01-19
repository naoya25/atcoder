def main():
    arr = tuple([input() for _ in range(3)])
    if "ABC" not in arr:
        print("ABC")
    elif "ARC" not in arr:
        print("ARC")
    elif "AGC" not in arr:
        print("AGC")
    elif "AHC" not in arr:
        print("AHC")

    return


if __name__ == "__main__":
    main()
