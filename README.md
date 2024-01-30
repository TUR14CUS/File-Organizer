# File Organizer Script

This Python script organizes files in a specified directory by deleting duplicate files and categorizing them into subdirectories based on file extensions. It provides options for the user to input the directory path and monitors the directory for new files, ensuring proper organization.

## Table of Contents
1. [Features](#features)
2. [How to Use](#how-to-use)
3. [Options](#options)
4. [User Input](#user-input)
5. [Requirements](#requirements)
6. [Notes](#notes)
7. [License](#license)

## Features

1. **Delete Duplicate Files**: The script identifies and deletes duplicate files in the specified directory.

2. **Categorize Files**: Files are categorized into subdirectories based on their file extensions. Categories include Images, PDFs, Datasets, and Videos.

3. **Monitor Directory**: The script continuously monitors the specified directory for new files and organizes them accordingly.

## How to Use

1. Run the script by executing the Python file.
   ```bash
   python file_organizer.py
   ```

2. Enter the path to the directory you want to organize when prompted.

3. The script will delete duplicate files, categorize existing files, and continuously monitor the directory for new files.

## Options

- **Delete Duplicate Files**: The script checks for duplicate files and deletes them.

- **Categorize Files**: Files are categorized into subdirectories based on predefined categories.

- **Monitor Directory**: The script continually monitors the specified directory for new files.

## User Input

- **Directory Path**: Enter the path to the directory you want to organize.

## Requirements

- Python 3.x
- External libraries: `os`, `re`, `time`

## Notes

- Ensure the specified directory exists and is not empty before running the script.

- The script creates subdirectories for each file category if they do not already exist.

- The script is designed to run continuously and classify new files in real-time.

## License
This project is licensed under the [MIT License](LICENSE).
