import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')

def print_animals_data():
    for animal in animals_data:
        name = animal["name"]
        diet = animal["characteristics"].get("diet")
        animal_type = animal["characteristics"].get("type")
        locations = ", ".join(animal.get("locations", []))

        print(f" Name: {name}")
        print(f" Diet: {diet}")
        print(f" Type: {animal_type}")
        print(f" Locations: {locations}")
        print()

print_animals_data()