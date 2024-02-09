import json

# Function to compare two sets of data
def compare_data(existing_data, new_data):
    new_entries = []
    for new_entry in new_data:
        if new_entry not in existing_data:
            new_entries.append(new_entry)
    return new_entries if new_entries else None

# Load existing data from the first JSON file
with open('existing_data.json', 'r') as file:
    existing_data = json.load(file)

# Load new data from the second JSON file
with open('new_removed_data.json', 'r') as file:
    new_data = json.load(file)

# Compare the two sets of data
result = compare_data(existing_data, new_data)

# Print the result
if result:
    with open('result_unique_data.json', 'w') as file:
        json.dump(result, file, indent=4)
else:
    if len(existing_data) - len(new_data) == 1:
        missing_entry = [entry for entry in existing_data if entry not in new_data][0]
        with open('result_missing_data.json', 'w') as file:
            json.dump(missing_entry, file, indent=4)
    else:
        with open('result_result_add_new_data.json', 'w') as file:
            file.write("null")
