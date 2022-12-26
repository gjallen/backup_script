import os
import json

# Set the directory to scan
directory = '/path/to/directory'

# Load the file information from the JSON file
with open('files.json', 'r') as f:
    files = json.load(f)

# Create a dictionary to store the current file information
current_files = {}

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
        current_files[file_path] = file_info

# Compare the file information in the JSON file to the current file information
for file in files:
    current_file_info = current_files.get(file['path'])
    if current_file_info:
        # Update the file information in the JSON file if it has changed
        if current_file_info != file:
            file.update(current_file_info)
    else:
        # Remove the file from the JSON file if it no longer exists
        files.remove(file)

# Add new files to the JSON file
for file_path, file_info in current_files.items():
    if file_info not in files:
        files.append(file_info)

# Save the updated file information to the JSON file
with open('files.json', 'w') as f:
    json.dump(files, f)
