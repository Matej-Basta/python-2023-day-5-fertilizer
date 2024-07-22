import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    args = parser.parse_args()

    try:
        with open(args.input_file, "r") as input_file:
            almanac = extract_numbers(input_file)
            
            smallest_location = float("inf")
            for seed in almanac["seeds"]:
                location = get_location(seed, almanac)
                smallest_location = location if location < smallest_location else smallest_location
            
            print(smallest_location)


    except FileNotFoundError:
        raise Exception("The file does not exist.")
    except:
        raise Exception("Something went wrong.")

def extract_numbers(input_file):
    almanac = {}
    current = None
    for line in input_file:
        print("here")
        if line == "\n":
            continue
        elif "seeds" in line:
            almanac["seeds"] = [int(x) for x in line.split(":")[-1].split()]
        elif "seed-to-soil" in line:
            almanac["seed_to_soil"] = {}
            current = "soil"
            continue
        elif "soil-to-fertilizer" in line:
            almanac["soil_to_fertilizer"] = {}
            current = "fertilizer"
            continue
        elif "fertilizer-to-water" in line:
            almanac["fertilizer_to_water"] = {}
            current = "water"
            continue
        elif "water-to-light" in line:
            almanac["water_to_light"] = {}
            current = "light"
            continue
        elif "light-to-temperature" in line:
            almanac["light_to_temperature"] = {}
            current = "temperature"
            continue
        elif "temperature-to-humidity" in line:
            almanac["temperature_to_humidity"] = {}
            current = "humidity"
            continue
        elif "humidity-to-location" in line:
            almanac["humidity_to_location"] = {}
            current = "location"
            continue
        else:
            data = [int(x) for x in line.split()]
            match current:
                case "soil":
                    for i in range(data[-1]):
                        almanac["seed_to_soil"][data[1] + i] = data[0] + i
                case "fertilizer":
                    for i in range(data[-1]):
                        almanac["soil_to_fertilizer"][data[1] + i] = data[0] + i
                case "water":
                    for i in range(data[-1]):
                        almanac["fertilizer_to_water"][data[1] + i] = data[0] + i
                case "light":
                    for i in range(data[-1]):
                        almanac["water_to_light"][data[1] + i] = data[0] + i
                case "temperature":
                    for i in range(data[-1]):
                        almanac["light_to_temperature"][data[1] + i] = data[0] + i
                case "humidity":
                    for i in range(data[-1]):
                        almanac["temperature_to_humidity"][data[1] + i] = data[0] + i
                case "location":
                    for i in range(data[-1]):
                        almanac["humidity_to_location"][data[1] + i] = data[0] + i
    return almanac


def get_soil(seed, seed_soil_map):
    if soil := seed_soil_map.get(seed):
        return soil
    else:
        return seed

def get_fertilizer(soil, soil_fertilizer_map):
    if fertilizer := soil_fertilizer_map.get(soil):
        return fertilizer
    else:
        return soil

def get_water(fertilizer, fertilizer_water_map):
    if water := fertilizer_water_map.get(fertilizer):
        return water
    else:
        return fertilizer

def get_light(water, water_light_map):
    if light := water_light_map.get(water):
        return light
    else:
        return water

def get_temperature(light, light_temperature_map):
    if temperature := light_temperature_map.get(light):
        return temperature
    else:
        return light

def get_humidity(temperature, temperature_humidity_map):
    if humidity := temperature_humidity_map.get(temperature):
        return humidity
    else:
        return temperature

def get_location(seed, almanac):
    soil = get_soil(seed, almanac["seed_to_soil"])
    fertilizer = get_fertilizer(soil, almanac["soil_to_fertilizer"])
    water = get_water(fertilizer, almanac["fertilizer_to_water"])
    light = get_light(water, almanac["water_to_light"])
    temperature = get_temperature(light, almanac["light_to_temperature"])
    humidity = get_humidity(temperature, almanac["temperature_to_humidity"])
    if location := almanac["humidity_to_location"].get(humidity):
        return location
    else:
        return humidity

if __name__ == "__main__":
    main()