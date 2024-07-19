import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    try:
        with open(args.input_file, "r") as input_file:
            almanac = extract_numbers(input_file)
            
            print(almanac)
            print("--------------")


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

def extract_numbers(input_file):
    almanac = {}
    current = None
    for line in input_file:
        if line == "\n":
            continue
        elif "seeds" in line:
            almanac["seeds"] = line.split(":")[-1].split()
        elif "seed-to-soil" in line:
            current = "soil"
            continue
        elif "soil-to-fertilizer" in line:
            current = "fertilizer"
            continue
        elif "fertilizer-to-water" in line:
            current = "water"
            continue
        elif "water-to-light" in line:
            current = "light"
            continue
        elif "light-to-temperature" in line:
            current = "temperature"
            continue
        elif "temperature-to-humidity" in line:
            current = "humidity"
            continue
        elif "humidity-to-location" in line:
            current = "location"
            continue
        else:
            match current:
                case "soil":
                    almanac["seed_to_soil"] = line.split()
                case "fertilizer":
                    almanac["soil_to_fertilizer"] = line.split()
                case "water":
                    almanac["fertilizer_to_water"] = line.split()
                case "light":
                    almanac["water_to_light"] = line.split()
                case "temperature":
                    almanac["light_to_temperature"] = line.split()
                case "humidity":
                    almanac["temperature_to_humidity"] = line.split()
                case "location":
                    almanac["humidity_to_location"] = line.split()

    return almanac


def get_soil(seed, seed_soil_map):
    if soil := seed_soil_map.get(seed):
        return soil
    else:
        return seed

if __name__ == "__main__":
    main()