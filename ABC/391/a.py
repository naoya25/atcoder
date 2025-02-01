def main():
    d = input()
    direction_map = {
        "N": "S",
        "E": "W",
        "W": "E",
        "S": "N",
        "NE": "SW",
        "NW": "SE",
        "SE": "NW",
        "SW": "NE",
    }
    print(direction_map[d])
    return


if __name__ == "__main__":
    main()
