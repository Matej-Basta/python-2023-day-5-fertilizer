import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    try:
        with open(args.input_file, "r") as input_file:
            soil = [[50, 98, 2], [52, 50, 48]]
            seed_soil_map = {}
            for list in soil:
                for i in range(list[-1]):
                    seed_soil_map[list[1] + i] = list[0] + i

            print(get_soil(98, seed_soil_map))
    except FileNotFoundError:
        raise Exception("The file does not exist.")
    except:
        raise Exception("Something went wrong.")

def get_soil(seed, seed_soil_map):
    if soil := seed_soil_map.get(seed):
        return soil
    else:
        return seed

if __name__ == "__main__":
    main()