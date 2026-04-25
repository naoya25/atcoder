def main():
    s = input()
    world, stage = s.split("-")
    world = int(world)
    stage = int(stage)

    if stage < 8:
        print(f"{world}-{stage + 1}")
    elif world < 8 and stage == 8:
        print(f"{world + 1}-1")

    return


if __name__ == "__main__":
    main()
