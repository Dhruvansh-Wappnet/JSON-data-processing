import json
import time

# Function to compare two sets of data
def compare_data(existing_data, new_data):
    changes = [entry for entry in new_data if entry not in existing_data]
    return changes if changes else None

# Start measuring the execution time
start_time = time.time()

# Load existing data from the first JSON file
with open('existing_data.json', 'r') as file:
    existing_data = json.load(file)

# Load new data from the second JSON file
with open('new_add_data.json', 'r') as file:
    new_data = json.load(file)

# Compare the two sets of data to find changes
changes = compare_data(existing_data, new_data)

# Update existing data based on changes
if changes:
    for change in changes:
        # Remove existing entry with the same ID, if present
        existing_data = [entry for entry in existing_data if entry['id'] != change['id']]
        # Add the new entry
        existing_data.append(change)

    # Write the updated data to the existing_data.json file
    with open('existing_data.json', 'w') as file:
        json.dump(existing_data, file, indent=4)
else:
    # Check if new data lacks some entries from existing data
    missing_entries = [entry for entry in existing_data if entry not in new_data]
    if missing_entries:
        # Write missing entries to a new JSON file
        with open('result_missing_data.json', 'w') as file:
            json.dump(missing_entries, file, indent=4)
    else:
        # Write "null" to a separate JSON file
        with open('result_null.json', 'w') as file:
            file.write("null")

# Calculate the total execution time
end_time = time.time()
total_time = end_time - start_time
print("Total execution time:", total_time * 1000, "milliseconds")
