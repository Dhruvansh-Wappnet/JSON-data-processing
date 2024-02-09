import json

file_path = 'existing_data.json'
with open(file_path, 'r') as file:
    data = json.load(file)   # load the JSON object from the file
    
# print(data)


# Dictionary to store unique values for each field
unique_values = {}

# Find fields with duplicate values
for entry in data:
    for field, value in entry.items():
        if value in unique_values:
            unique_values[value].append(field)
        else:
            unique_values[value] = [field]

# Generate new data for fields with duplicates and update the existing data
for value, fields in unique_values.items():
    if len(fields) > 1:
        for i in range(len(fields)):
            for entry in data:
                if entry[fields[i]] == value:
                    for field in fields:
                        if field == fields[i]:
                            entry[field] = f"unique_{field}_{value}_{i+1}"
                        else:
                            entry[field] = value

# Print the updated data
print(json.dumps(data, indent=4))
print(len(data))

with open('existing_data.json', 'w') as file:
     json.dump(data, file, indent=4)

