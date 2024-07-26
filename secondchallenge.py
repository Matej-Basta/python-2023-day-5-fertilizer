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

                location = 0
                valid_seed = False
                while not valid_seed:
                    print(location)
                    seed = get_seed(location, almanac)
                    if is_seed_valid(seed, almanac["seeds"]):
                        valid_seed = True
                        print(location)
                    location += 1

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

def is_seed_valid(seed, seeds):
    for seed_start, count in zip(seeds[::2], seeds[1::2]):
        if seed >= seed_start and seed < seed_start + count:
            return True               
    return False

def get_humidity(location, humidity_location):
    for section in humidity_location:
        if location >= section[0] and location <= section[0] + section[-1]:
            return section[1] + location - section[0]
    return location

def get_temperature(humidity, temperature_humidity):
    for section in temperature_humidity:
        if humidity >= section[0] and humidity <= section[0] + section[-1]:
            return section[1] + humidity - section[0]
    return humidity

def get_light(temperature, light_temperature):
    for section in light_temperature:
        if temperature >= section[0] and temperature <= section[0] + section[-1]:
            return section[1] + temperature - section[0]
    return temperature

def get_water(light, water_ligth):
    for section in water_ligth:
        if light >= section[0] and light <= section[0] + section[-1]:
            return section[1] + light - section[0]
    return light

def get_fertilizer(water, fertilizer_water):
    for section in fertilizer_water:
        if water >= section[0] and water <= section[0] + section[-1]:
            return section[1] + water - section[0]
    return water

def get_soil(fertilizer, soil_fertilizer):
    for section in soil_fertilizer:
        if fertilizer >= section[0] and fertilizer <= section[0] + section[-1]:
            return section[1] + fertilizer - section[0]
    return fertilizer

def get_seed(location, almanac):
    humidity = get_humidity(location, almanac["humidity_to_location"])
    temperature = get_temperature(humidity, almanac["temperature_to_humidity"])
    light = get_light(temperature, almanac["light_to_temperature"])
    water = get_water(light, almanac["water_to_light"])
    fertilizer = get_fertilizer(water, almanac["fertilizer_to_water"])
    soil = get_soil(fertilizer, almanac["soil_to_fertilizer"])
    for section in almanac["seed_to_soil"]:
        if soil >= section[0] and soil <= section[0] + section[-1]:
            return section[1] + soil - section[0]
    return soil

if __name__ == "__main__":
    main()