def main():
    n = int(input())
    a = list(map(int, input().split()))
    people = [a[0]]
    for i in range(1, n):
        people.append(a[i] + people[i - 1])
    min_people = min(people)
    if min_people < 0:
        people = list(map(lambda x: x - min_people, people))

    print(people[-1])


if __name__ == "__main__":
    main()
