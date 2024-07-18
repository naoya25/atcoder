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


import numpy as np

a = np.array([1, 1, 0])
b = np.array([2, 0, 0])
c = np.cross(a, b)
d = np.cross(b, a)
print(c)
print(d)
