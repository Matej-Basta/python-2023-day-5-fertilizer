def main():
    soil = [[50, 98, 2], [52, 50, 48]]

    seed_soil_map = {}
    for list in soil:
        for i in range(list[-1]):
            seed_soil_map[list[1] + i] = list[0] + i

    print(get_soil(98, seed_soil_map))

def get_soil(seed, seed_soil_map):
    if soil := seed_soil_map.get(seed):
        return soil
    else:
        return seed

if __name__ == "__main__":
    main()