def main():
    a_sum = sum(map(int, input().split()))
    b_sum = sum(map(int, input().split()))
    print(a_sum - b_sum + 1)


if __name__ == "__main__":
    main()
