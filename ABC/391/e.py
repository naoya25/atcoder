import sys

sys.setrecursionlimit(10**7)


def main():
    def apply_majority_operation(arr):
        if len(arr) == 1:
            return arr
        next_arr = []
        for i in range(0, len(arr), 3):
            majority = sum(int(arr[i + j]) for j in range(3))
            next_arr.append("1" if majority >= 2 else "0")
        return apply_majority_operation(next_arr)

    def find_min_changes(arr, target):
        n = len(arr)
        if n == 1:
            return 0 if arr[0] == target else 1

        next_target = target
        min_changes = float("inf")
        for bit in ["0", "1"]:
            changes = 0
            next_arr = []
            for i in range(0, n, 3):
                group = arr[i : i + 3]
                majority = sum(int(group[j]) for j in range(3))
                current_majority = "1" if majority >= 2 else "0"
                if current_majority != bit:
                    changes += 3 - majority if bit == "1" else majority
                next_arr.append(bit)

            changes += find_min_changes(next_arr, next_target)
            min_changes = min(min_changes, changes)

        return min_changes

    n = int(input())
    a = input()

    final_value = apply_majority_operation(a)[0]

    target_value = "1" if final_value == "0" else "0"
    result = find_min_changes(a, target_value)

    print(result)


if __name__ == "__main__":
    main()
