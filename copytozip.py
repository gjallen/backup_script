import os
import json
import zipfile
from datetime import datetime

# Load the file information from the JSON file
with open('files.json', 'r') as f:
    files = json.load(f)

# Create the zip file with the current date and time as the file name
date_time = datetime.now().strftime('%Y%m%d_%H%M%S')
zip_file_name = f'{date_time}.zip'
zip_file = zipfile.ZipFile(zip_file_name, 'w')

# Add the files to the zip file
for file in files:
    zip_file.write(file['path'])

# Close the zip file
zip_file.close()
