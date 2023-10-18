import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, dest_dir):
    """
    Backup files from source directory to destination directory.
    
    Parameters:
        source_dir (str): The source directory path.
        dest_dir (str): The destination directory path.
    """
    try:
        # Check if source and destination directories exist
        if not os.path.exists(source_dir):
            print(f"Error: Source directory {source_dir} does not exist.")
            return
        
        if not os.path.exists(dest_dir):
            print(f"Error: Destination directory {dest_dir} does not exist.")
            return
        
        for filename in os.listdir(source_dir):
            source_file_path = os.path.join(source_dir, filename)
            dest_file_path = os.path.join(dest_dir, filename)
            
            # Separate filename and extension
            name, ext = os.path.splitext(filename)
            
            # If file already exists in destination, append timestamp
            if os.path.exists(dest_file_path):
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                dest_file_path = os.path.join(dest_dir, f"{name}_{timestamp}{ext}")
            
            shutil.copy2(source_file_path, dest_file_path)
            print(f"Successfully copied {filename} to {dest_file_path}")
            
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python python_assignment_4.py /path/to/source /path/to/destination")
    else:
        source_dir = sys.argv[1]
        dest_dir = sys.argv[2]
        backup_files(source_dir, dest_dir)
