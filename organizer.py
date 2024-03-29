import os
import re
import time

def delete_duplicate_files(dir_path):
    # Get a list of all the files in the directory
    files = os.listdir(dir_path)

    # Iterate through each file
    for file in files:
        # Check if the file has a duplicate version with a number in parentheses
        match = re.search(r'(.*)\s+\((\d+)\)\.(.*)', file)
        if match:
            # Get the base name and extension of the original file
            base_name = match.group(1)
            extension = match.group(3)
            original_file = base_name + '.' + extension

            # Check if the original file exists in the directory
            if original_file in files:
                # If it does, delete the duplicate file
                os.remove(os.path.join(dir_path, file))

def classify_file(directory, filename, categories):
    # Find the file extension
    extension = filename.split('.')[-1]

    # Iterate over the categories
    for category, extensions in categories.items():
        # If the extension matches one of the extensions in the category, move the file
        if extension in extensions:
            # Construct the file paths
            source_path = os.path.join(directory, filename)
            dest_path = os.path.join(directory, category, filename)

            # Move the file
            os.rename(source_path, dest_path)
            print(f'Moved {filename} to {category}')
            break

def monitor_directory(directory, categories):
    # Classify all existing files in the directory
    for filename in os.listdir(directory):
        classify_file(directory, filename, categories)

    # Initial list of files in the directory
    initial_files = os.listdir(directory)

    while True:
        # List of files in the directory after a short sleep
        time.sleep(5)
        current_files = os.listdir(directory)

        # Find the new files
        new_files = list(set(current_files) - set(initial_files))

        # Classify the new files
        for filename in new_files:
            classify_file(directory, filename, categories)

        # Update the initial list of files
        initial_files = current_files

if __name__ == "__main__":
    # User Inputs
    directory_path = input("Enter the path to the directory: ").strip()

    # Dictionary of file categories and their extensions
    categories = {
        'Images': ['jpeg', 'jpg', 'png'],
        'PDFs': ['pdf'],
        'Datasets': ['csv', 'xlsx', 'json'],
        'Videos': ['mp4']
    }

    # Ensure the directory exists
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        exit()

    # Ensure the directory is not empty
    if not os.listdir(directory_path):
        print(f"Directory '{directory_path}' is empty.")
        exit()

    # Ensure the directory contains subdirectories for categories
    for category in categories:
        category_path = os.path.join(directory_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    # Delete duplicate files
    delete_duplicate_files(directory_path)

    # Monitor and classify files
    monitor_directory(directory_path, categories)
