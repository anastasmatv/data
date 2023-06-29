import json

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Write data to a JSON file
with open("data.json", "w") as file:
    json.dump(data, file)

# Read data from a JSON file
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)
