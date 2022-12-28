import os
import subprocess
import shutil

# 
nfs_share_url = '10.0.0.24:/mnt/nfs_k3s'
mount_point = '/mnt/nfs'

if not os.path.exists(mount_point):
    os.makedirs(mount_point)

subprocess.run(['mount', nfs_share_url, mount_point])

# Set the source and destination directories
src_dir = '/home/folder1'
dst_dir = mount_point

# Set the log file path
log_file = '/home/folder1/file.log'

# Open the log file in write mode
with open(log_file, 'w') as f:
    # Iterate over all the files in the source directory
    for filename in os.listdir(src_dir):
        # Construct the full path to the file
        src_path = os.path.join(src_dir, filename)
        dst_path = os.path.join(dst_dir, filename)
        try:
            # Copy the file from the source to the destination
            shutil.copy2(src_path, dst_path)
            # Write a message to the log file indicating the file was backed up successfully
            f.write(f'Successfully backed up {src_path} to {dst_path}\n')
        except Exception as e:
            # Write an error message to the log file if there was a problem backing up the file
            f.write(f'Error backing up {src_path}: {e}\n')


