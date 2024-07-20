def main():
    x = list(input())
    if len(set(x)) == 1:
        print("Weak")
        return

    for i in range(3):
        if x[i + 1] != str(int(x[i]) + 1)[-1]:
            print("Strong")
            return
    print("Weak")
    return


if __name__ == "__main__":
    main()
