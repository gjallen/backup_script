import os
import json

# Set the directory to scan
directory = '/path/to/directory'

# Initialize an empty list to store the file information
files = []

# Iterate through the directory and get the file information
for root, dirs, file_names in os.walk(directory):
    for file_name in file_names:
        file_path = os.path.join(root, file_name)
        file_info = {
            'name': file_name,
            'path': file_path,
            'size': os.stat(file_path).st_size,
            'modified_time': os.stat(file_path).st_mtime
        }
        files.append(file_info)

# Save the file information to a JSON file
with open('files.json', 'w') as f:
    json.dump(files, f)
