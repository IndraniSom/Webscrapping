import json

# Load the data from the JSON file
with open('faculty.json', 'r') as file:
    data = json.load(file)

# Create a list to store the mapped data
mapped_data = []

# Loop over each row in the data, skipping the first one (headers)
for row in data[1:]:
    # Create a dictionary for the row
    row_dict = {
        'nameofthefaculty': row[0],
        'desg': row[1],
        'highest qualification': row[2],
        'experience': row[3]
    }

    # Add the dictionary to the mapped_data list
    mapped_data.append(row_dict)

# Write the mapped data to a new JSON file
with open('mapped_faculty.json', 'w') as file:
    json.dump(mapped_data, file)