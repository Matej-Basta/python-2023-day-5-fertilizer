import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    args = parser.parse_args()

    try:
        with open(args.input_file, "r") as input_file:
            with open(args.output_file, "w") as output_file:
                almanac = extract_numbers(input_file)

                lowest_location = float("inf")
                for seed in almanac["seeds"]:
                    new_location = get_location(seed, almanac)
                    lowest_location = min(lowest_location, new_location)
                
                print(lowest_location)
                output_file.write(str(lowest_location))

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
            almanac["seeds"] = [int(x) for x in line.split(":")[-1].split()]
        elif "seed-to-soil" in line:
            almanac["seed_to_soil"] = []
            current = "soil"
            continue
        elif "soil-to-fertilizer" in line:
            almanac["soil_to_fertilizer"] = []
            current = "fertilizer"
            continue
        elif "fertilizer-to-water" in line:
            almanac["fertilizer_to_water"] = []
            current = "water"
            continue
        elif "water-to-light" in line:
            almanac["water_to_light"] = []
            current = "light"
            continue
        elif "light-to-temperature" in line:
            almanac["light_to_temperature"] = []
            current = "temperature"
            continue
        elif "temperature-to-humidity" in line:
            almanac["temperature_to_humidity"] = []
            current = "humidity"
            continue
        elif "humidity-to-location" in line:
            almanac["humidity_to_location"] = []
            current = "location"
            continue
        else:
            data = [int(x) for x in line.split()]
            match current:
                case "soil":
                    almanac["seed_to_soil"].append(data)
                case "fertilizer":
                    almanac["soil_to_fertilizer"].append(data)
                case "water":
                    almanac["fertilizer_to_water"].append(data)
                case "light":
                    almanac["water_to_light"].append(data)
                case "temperature":
                    almanac["light_to_temperature"].append(data)
                case "humidity":
                    almanac["temperature_to_humidity"].append(data)
                case "location":
                    almanac["humidity_to_location"].append(data)
    return almanac


def get_soil(seed, seed_soil):
    for section in seed_soil:
        if seed >= section[1] and seed <= section[1] + section[-1]:
            return section[0] + seed - section[1]
    return seed

def get_fertilizer(soil, soil_fertilizer):
    for section in soil_fertilizer:
        if soil >= section[1] and soil <= section[1] + section[-1]:
            return section[0] + soil - section[1]
    return soil

def get_water(fertilizer, fertilizer_water):
    for section in fertilizer_water:
        if fertilizer >= section[1] and fertilizer <= section[1] + section[-1]:
            return section[0] + fertilizer - section[1]
    return fertilizer

def get_light(water, water_light):
    for section in water_light:
        if water >= section[1] and water <= section[1] + section[-1]:
            return section[0] + water - section[1]
    return water

def get_temperature(light, light_temperature):
    for section in light_temperature:
        if light >= section[1] and light <= section[1] + section[-1]:
            return section[0] + light - section[1]
    return light

def get_humidity(temperature, temperature_humidity):
    for section in temperature_humidity:
        if temperature >= section[1] and temperature <= section[1] + section[-1]:
            return section[0] + temperature - section[1]
    return temperature

def get_location(seed, almanac):
    soil = get_soil(seed, almanac["seed_to_soil"])
    fertilizer = get_fertilizer(soil, almanac["soil_to_fertilizer"])
    water = get_water(fertilizer, almanac["fertilizer_to_water"])
    light = get_light(water, almanac["water_to_light"])
    temperature = get_temperature(light, almanac["light_to_temperature"])
    humidity = get_humidity(temperature, almanac["temperature_to_humidity"])
    for section in almanac["humidity_to_location"]:
        if humidity >= section[1] and humidity <= section[1] + section[-1]:
            return section[0] + humidity - section[1]
    return humidity

if __name__ == "__main__":
    main()