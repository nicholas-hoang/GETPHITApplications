#Folder Generator Script
#Author: Nicholas Hoang, GRA at UTHealth School of Biomedical Informatics
#Date: 05/19/2023


# Install Requirements from requirements.txt
import os
import pandas as pd
import numpy as np
import shutil
import pathlib
import glob
from openpyxl import load_workbook


class BootCamp:

    def __init__(self, file, evaluation):
        self.file = file
        self.evaluation = 'Evaluation_Rubric.xlsx'

    def load_data(self):
        student_registration = pd.read_excel(self.file)
        student_registration = student_registration.rename(columns={
            'Registration Date': 'Registration_Date',
            'First Name': 'First_Name',
            'Last Name': 'Last_Name'})

        student_registration.Registration_Date = student_registration.Registration_Date.dt.strftime(
            '%m/%d/%Y')

        evaluation_form = pd.read_excel(self.evaluation)

        return student_registration, evaluation_form


def get_first_last_name(row):
    fullname = row.First_Name + " " + row.Last_Name
    return fullname


def get_existing_folders():
    """ get_existing_folders() function checks the current directory for existing folders and returns a list of the folders found.
    """
    num_of_docs = [directory for directory in os.listdir(
        '.') if os.path.isdir(os.path.join(".", directory))]
    print(
        f'There are a total of {len(num_of_docs)} student folders in this directory.')
    return num_of_docs


def create_new_folders(dataframe):
    """Create a new folder for each student in the dataframe.
       Function will check for existing folders and ignore those students.
    """
    
    if dataframe.empty:
        print("Empty dataframe. No student folders were generated.")
        return

    count = 0
    student_names = pd.Series(dataframe.full_name)

    for student in student_names:
        folder_name = student.title()
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)  # Create Student Folder
            count += 1

    print(f"A total of {count} student folders were generated.")


def fill_folders():
    """ fill_folders(evaluation_form): takes the evaluation form and places it in each student folder.
    """
    source = 'Evaluation_Rubric.xlsx'
    path = pathlib.Path('.')
# Put Evaluation Form In Student Folders
    for item in path.iterdir():
        if item.is_dir():
            shutil.copy2(source, item)  # Place Form in Folder


def rename_files():
    """ rename_files() function renames the files in the student folders to the name of the folder.
    """
    path = pathlib.Path('.')
    for folder in path.iterdir():
        if folder.is_dir():
            for file in folder.iterdir():
                if file.is_file():
                    new_file = folder.name + file.suffix
                    file.rename(path / folder.name / new_file)


def writeStudentNames(registrations, evaluation):
    # Get a list of nested-files with extension .xlsx (example /student1/student1.xlsx)
    student_files = glob.glob('**/*.xlsx', recursive=True)

    # Exclude specific files from the list
    excluded_files = [registrations, evaluation]
    students = [file for file in student_files if file not in excluded_files]

    # Iterate through each file in student_files
    for student in students:
        try:
            # Load Workbook in Binary Mode
            print(f"Loading workbook for {student}")
            workbook = load_workbook(filename=student, read_only=False)

            # Define desired sheet names
            sheet = workbook['Evaluator 1']

            # Extract student name from filename
            student_name = os.path.splitext(os.path.basename(student))[0]

            # Define desired cell value
            sheet['B3'] = student_name

            # Save and close the workbook
            print(f"Saving workbook for {student}")
            workbook.save(filename=student)
            workbook.close()

        except KeyError as e:
            print(f"Error writing student name to {student}: {e}")
            continue


def main():
    studentRegistrations = input('Copy and paste the student registration file name:\n')
    BootCamp1 = BootCamp(studentRegistrations, 'Evaluation_Rubric.xlsx')
    df = BootCamp1.load_data()[0]
    print('=====================================================')
    get_existing_folders()
    print('=====================================================')
    df['full_name'] = df.apply(get_first_last_name, axis=1)
    create_new_folders(df)
    fill_folders()
    rename_files()
    writeStudentNames(studentRegistrations, 'Evaluation_Rubric.xlsx')
    print('All Folders Processed!')


if __name__ == "__main__":
    main()
