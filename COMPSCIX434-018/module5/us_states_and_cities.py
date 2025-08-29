import json
filename = 'us_states_and_cities.json'

try:
    with open(filename, 'r') as file:
        data = json.load(file)

    state_with_most_cities = None
    max_cities_count = 0

    for state, cities in data.items():
        num_cities = len(cities)
        if num_cities > max_cities_count:
            max_cities_count = num_cities
            state_with_most_cities = state

    print(f"{state_with_most_cities} has the most cities and the number of cities is {max_cities_count}")

    city_occurrence = {}
    for state, cities in data.items():
        for city in cities:
            if city in city_occurrence:
                city_occurrence[city] += 1
            else:
                city_occurrence[city] = 1

    max_city_occurrence = 0
    city_with_max_occurrence = None
    for city, occurrence in city_occurrence.items():
        if occurrence > max_city_occurrence:
            max_city_occurrence = occurrence
            city_with_max_occurrence = city

    print(f"The most common city name is {city_with_max_occurrence}, and {max_city_occurrence} states have that city")

except FileNotFoundError:
    print(f"Error: {filename} is not exist")
except json.JSONDecodeError:
    print(f"Error: {filename} is not in JSON format")
except Exception as e:
    print(f"Error: {str(e)}")