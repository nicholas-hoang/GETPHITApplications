# GETPHITApplications

# Folder Generator Script

This script is designed to generate folders for students based on a student registration file and perform various operations related to organizing and filling those folders.

## Author
- Nicholas Hoang, GRA at UTHealth School of Biomedical Informatics

## Date
- 05/19/2023

## Requirements
Ensure the following dependencies are installed:
- os
- pandas
- numpy
- shutil
- pathlib
- glob
- openpyxl

You can install the requirements by running the following command:
pip install -r requirements.txt


## Usage

The script consists of the following classes and functions:

### BootCamp Class

- `__init__(self, file, evaluation)`: Initializes the BootCamp class instance with the provided file and evaluation parameters.
- `load_data(self)`: Loads the student registration and evaluation form data from the specified files.

### Functions

- `get_first_last_name(row)`: Returns the full name of a student by concatenating their first name and last name.
- `get_existing_folders()`: Checks the current directory for existing folders and returns a list of the folders found.
- `create_new_folders(dataframe)`: Creates a new folder for each student in the provided dataframe.
- `fill_folders()`: Copies the evaluation form to each student folder.
- `rename_files()`: Renames the files in the student folders to match the folder names.
- `writeStudentNames(registrations, evaluation)`: Writes the student names to the corresponding files in each student folder.
- `main()`: The main entry point of the script.

To use the script, follow these steps:

1. Install the required dependencies using the provided `requirements.txt` file.
2. Run the script.
3. When prompted, copy and paste the name of the student registration file.
4. The script will generate new folders for each student, copy the evaluation form to each folder, rename the files, and write the student names to the corresponding files.
5. Once all folders are processed, the script will display a completion message.

Note: Ensure that the student registration file and the evaluation form file are in the same directory as the script.

Feel free to modify the script and adapt it to your specific needs!

