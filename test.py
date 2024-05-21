import random


def main():
    for i in range(41, 50):
        rand_ans = random.choice(["A", "B", "C", "D"])
        print(f"{i}.{rand_ans}", end=", ")
    else:
        print("\n")
    return


if __name__ == "__main__":
    main()
